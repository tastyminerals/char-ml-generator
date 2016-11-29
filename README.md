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


### USAGE
The script requires some text corpus to train on. Small scale English, Russian and Chinese corpora are located in the `corpora` directory. Here are few usage examples.

- Train some corpus with history length = 10 characters
`python char_ml_generator.py -f ROCStories_2016.txt -p 10`

- Generate 2000 characters (1000 by default)
`python char_ml_generator.py -m ROCStories_2016.txt.pickle -g 2000`


- Generated from English ROCStories corpus
```
Overweight Kid. Dan's parents took us anyway. We ended up sleeping in the future.
No Kidding. Joan got mad when she happened upon a family trip there. It wasn't fair. When we got back!
Lisa wanted to make sure she wouldn't sell Tim the gun with no ID.
Tough Tim. Tim loved dancing. Her mom was going to the movies. Jane and Michael went to the beauty pageant. It was christmas morning!
Bacon Thief. We fried a lot of algae growing on his furniture. Then she went to see a doctor. So she ate them. 
Tina was drinking a juice box from the fridge. But Adam didn't hesitate to rush right over to help her put shoes on her doll. 
Her mother told him that was a writing teacher. He decided to buy a decent priced convertible 
Hole in Pocket. Vanity was walking down the road one day really fast. He was trying to reach high ground. 
Just as Jake got to the point. One evening he met Bernice, and bought hot dogs and made note of the rings she loved.

```

- Generated from Russian news crawl corpus

```
Без единой тенденции закрылись торги на европейских рынках акций, ведущие фондовые индексы прибавили от 3 до 6%.
Во-вторых, Единая аграрная политика сделала шаг вперед, и Италия смогла принять участие в региональном саммите по этой проблеме самостоятельно выпустить свой фильм в румынский прокат, чтобы начать клинические испытания – как это делается
Организаторы "Грэмми" ищут способ повысить популярность премьер-министра Сомчая Вонгсавата, которого они требуют отправить в отставку действующий кабинет – уже четвертая по счету.
Такая динамика стала реакцией на решение израильского Верховного суда в Гааге большинством в парламенте появится оппозиция, я считаю, что безусловным приоритетом для нас является защита жизни и достоинства российских каналов на вещание на территории сектора Газа из-за продолжающихся боев между правительственными силами и воюющими группами, при условии, что министры связи ЕС одобрят на заседании в среду сторона обвинения потребовала от правительственных войск Афганистана погибли и четверо были ранены, один тяжело.
Большинство из 202 погибших составили гражданские специалисты в своей области, отобранные со всей Европы сами проектируют воздушные шары и дирижабли, сами запускают их в шведских лесах, и сами анализируют полученные после полета данные.
```

- Generated from Chinese twitter corpus

```
是的，女足世界杯日程表，一边看，一边想蒙着眼睛发财，先进的东西不能一次吃到排骨绿豆汤。。。凉瓜是啥。。
RT:
草巨巨生日快乐？果断翻墙并围观之。那个人应该都还不知道我为什么不能把形象工程，看官商勾结我无罪，你们赶紧洗洗睡
其实我同意,只是那18个人全站着，这是一种什么样的专业，也无所谓，与原来的相比，还是有很多美女的。
测试短信发推
用itweetdeck有点复杂，带点影射，最后带点希望，政治阴谋片大概就是这种天气似乎应该重新去看一遍
发现一天要是不信天气预报，未来三天天气良好哦也，所以希望能弄下来吧……
QAQ我昨晚拍死了6只后就不来找我了！哈！
```
