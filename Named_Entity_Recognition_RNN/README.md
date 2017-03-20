This is an attempt to implement Named Entity Recognition, an important concept in Natural Language Processing by using sequence to sequence models. I have used the same functions as used in machine translation. I have created two languages - one is the original natural language query, and the other is the same query with the named entities replaced with their tag name. For example

Language 1: Sundar Pichchai is heading Google from its headquarters in Mountain View
Language 2: PERSON PERSON is heading LISTING from its headquarters in LOCATION LOCATION

I am trying to model this as a machine translation problem. I trained this on around 1 million language pairs, but the model was heavily overfitting. Right now I am training on a a much larger dataset of Google News, however due to lack of very good hardware, it is taking a lot of time. 