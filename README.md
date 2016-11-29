# char-ml-generator
Tiny character based [maximum likelihood](https://en.wikipedia.org/wiki/Maximum_likelihood_estimation) [language model](https://en.wikipedia.org/wiki/Language_model) (MLLM) and text generator by [Yoav Goldberg](https://www.cs.bgu.ac.il/~yoavg/uni/). Nice to play with some random corpora and also use as a baseline.

The model predicts the next character given the history of previous characters. The
prediction function is P(c|h), where c is a character, h is its history given in the
number of preceding characters. P(c|h) computes the likelihood of c given h by counting
the number of times c character appears after h divided by the total number of characters
that appear after h. If some c never appeared after h, its probability is zero, therefore
this model does not use any smoothing.

Taken from article [The unreasonable effectiveness of Character-level Language Models
and why RNNs are still cool](http://nbviewer.jupyter.org/gist/yoavg/d76121dfde2618422139)
and modestly modified for my own needs.
