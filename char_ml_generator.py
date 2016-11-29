#!/usr/bin/env python3
"""
Tiny maximum likelihood character based language model (MLLM) and text generator
by Yoav Goldberg. Nice to play with some random corpora and also use as a baseline.

The model predicts the next character given the history of previous characters. The
prediction funtion is P(c|h), where c is a character, h is its history given in the
number of preceding characters. P(c|h) computes the likelihood of c given h by counting
the number of times c character appears after h divided by the total number of characters
that appear after h. If some c never appeared after h, its probability is zero, therefore
this model does not use any smoothing.

Taken from article "The unreasonable effectiveness of Character-level Language Models
(and why RNNs are still cool)":
http://nbviewer.jupyter.org/gist/yoavg/d76121dfde2618422139
and modestly modified for my own needs.

"""

import sys
import argparse
import pickle
import re
from collections import Counter, defaultdict as dd
from random import random


def read_file(fname):
    """Read the file and return its contents as plain text."""
    with open(fname, 'r') as fopen:
        fdata = fopen.read()
    return fdata


def save_model(model, fname):
    """Dump trained model"""
    fname += '.pickle'
    with open(fname, 'wb') as fopen:
        pickle.dump(model, fopen)
    print('Model saved under "{0}".'.format(fname))


def load_model(fname):
    """Load trained model"""
    with open(fname, 'rb') as fopen:
        model = pickle.load(fopen)
    return model


def check_history(model, history):
    """Check if model was trained with different history to avoid key errors."""
    if not model.get('~'*history):
        history = len([c for c in model if c.startswith('~') and c.endswith('~')][0])
        print('#'* 57)
        print("# WARNING: the model was trained with history length:{0} #".format(history))
        print("#         Falling back to model history length.         #")
        print('#', ' '*53, '#')
        print('#'*22, 'GENERATING!', '#'*22)
    return history


def train_char_model(text, prev_chars):
    """Train a character-based ML model."""
    # calc probabilities
    def normalize(counter):
        total = float(sum(counter.values()))
        return [(char, cnt/total) for char, cnt in counter.items()]
    print("Training...")
    model = dd(Counter)
    # padding the data with starting chars
    pad = "~" * prev_chars
    text = pad + text
    # counting history->char occurences
    for i in range(len(text) - prev_chars):
        history, char = text[i:i+prev_chars], text[i+prev_chars]
        model[history][char] += 1
    trained_model = {hist: normalize(chars) for hist, chars in model.items()}
    return trained_model


def generate_char(model, history, prev_chars):
    """Generate a letter given history."""
    history = history[-prev_chars:]
    distr = model.get(history)
    rnd = random()
    # randomly sample most probable chars
    for char, prob in distr:
        rnd -= prob  # gradually subtract until good candidate
        if rnd <= 0:
            return char


def generate_text(model, prev_chars, length):
    """Generate text of some arbitrary length."""
    history = "~" * prev_chars
    chars = []
    for _ in range(length):
        new_char = generate_char(model, history, prev_chars)
        history = history[-prev_chars:] + new_char
        chars.append(new_char)
    return ''.join(chars)


def main():
    """Handle arguments, train the model and generate text."""
    if args.file and not args.nomodel:
        text = read_file(args.file)
        trained_model = train_char_model(text, args.prev)
        save_model(trained_model, args.file)
        sys.exit()
    if args.model:
        trained_model = load_model(args.model)
    if args.nomodel and args.file:
        trained_model = train_char_model(read_file(args.file), args.prev)
    # generate some random text
    history = check_history(trained_model, args.prev)
    gentext = generate_text(trained_model, history, args.gen)
    print(gentext)


if __name__ == '__main__':
    prs = argparse.ArgumentParser(description="""
    Tiny character-based ML text generator.""",
    formatter_class=argparse.RawTextHelpFormatter)
    prs.add_argument('-f', '--file',
                     help='Specify your training corpus (plain text) and train a model.',
                     required=False)
    prs.add_argument('-m', '--model',
                     help='Load a trained and previously saved model (pickle file).',
                     required=False)
    prs.add_argument('-g', '--gen', default=1000, type=int,
                     help='Specify the number of characters to generate (default 1000).',
                     required=False)
    prs.add_argument('-p', '--prev', default=8, type=int,
                     help='Specify the length of your training history in characters (default 8).',
                     required=False)
    prs.add_argument('-n', '--nomodel', action='store_true',
                     help="Don't store a model, just train and generate on the fly.",
                     required=False)
    args = prs.parse_args()
    main()
