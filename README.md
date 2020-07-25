# Understanding Points of Correspondence between Sentences for Abstractive Summarization
Dataset for our ACL SRW 2020 paper [Understanding Points of Correspondence between Sentences for Abstractive Summarization](https://www.aclweb.org/anthology/2020.acl-srw.26.pdf)

## Citation
```
@inproceedings{lebanoff-etal-2020-understanding,
    title = "Understanding Points of Correspondence between Sentences for Abstractive Summarization",
    author = "Lebanoff, Logan and Muchovej, John and Dernoncourt, Franck and Kim, Doo Soon and Wang, Lidan and Chang, Walter and Liu, Fei",
    booktitle = "Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics: Student Research Workshop",
    month = jul,
    year = "2020",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.acl-srw.26",
    pages = "191--198",
}
```

## Presentation Video
Watch our presentation given virtually at ACL:

[![Watch our presentation given virtually at ACL:](https://www.cs.ucf.edu/~feiliu/img/presentation_poc.png)](https://slideslive.com/38928667/understanding-points-of-correspondence-between-sentences-for-abstractive-summarization)

# Dataset
Fusing sentences containing disparate content is a remarkable human ability that helps create informative and succinct summaries. Such a simple task for humans has remained challenging for modern abstractive summarizers, substantially restricting their applicability in real-world scenarios. 

We present a dataset that contains 1,599 sentence fusion examples (taken from 1,174 documents) with fine-grained *Points of Correspondence* annotations. Points of correspondence (PoC) are cohesive devices that tie two sentences together into a coherent text. The types of points of correspondence are delineated by text cohesion theory, covering pronominal and nominal referencing, repetition and beyond. 

A point of correspondence is represented as a span of text from each sentence. Our dataset is in JSON format in the file `PoC_dataset.json`. 
Each example has the following attributes:

| Attribute | Content |
| --- | --- | 
| **Sentence_1** | Tokenized input sentence 1 |
| **Sentence_2** | Tokenized input sentence 2 |
| **Sentence_Fused** | Fused sentence created by merging Sentence_1 and Sentence_2 |
| **Sentence_1_Index** | Position of sentence in Full_Article |
| **Sentence_2_Index** | Position of sentence in Full_Article |
| **Sentence_Fused_Index** | Position of fused sentence in Full_Summary |
| **Full_Article** | Full CNN news article. Each sentence is separated by tabs |
| **Full_Summary** | Summary of the article. Each sentence is  separated by tabs |
| **PoCs** | List of Points of Correspondence |

Each PoC has the following attributes:

| Attribute | Content |
| --- | --- | 
| **Sentence_1_Selection** | Token indices for beginning and end of the PoC in input sentence |
| **Sentence_2_Selection** | Token indices for beginning and end of the PoC in input sentence |
| **Sentence_Fused_Selection** | Token indices for beginning and end of the PoC in fused sentence |
| **PoC_Type** | Can be any of `Nominal`, `Pronominal`, `Common-Noun`, `Repetition` and `Event` |

# Example Visualizations
We provide visualizations of every dataset example in the directory `PoC_visualizations/`, which can be opened in any browser, along with the code used to create them in `visualize_poc.py`.

The process is easy and can be seen below:

![Example visualization](points_of_correspondence.gif)

# Model Outputs
The outputs of our models can be downloaded here:
https://drive.google.com/file/d/10kFJopco2dd3C-jruOb-oVrOTuINnuSe/view?usp=sharing

*Note: We tested only on the examples that had at least one point of correspondence, so there are 1494 outputs for each model.
