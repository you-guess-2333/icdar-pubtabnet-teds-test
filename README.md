# This project is used to reproduce the BUG of the [teds evaluation tool](https://github.com/ibm-aur-nlp/PubTabNet/tree/master/src)

# Requirement
Python3


# Useage

First clone this repository
```
git clone --recursive https://github.com/you-guess-2333/icdar-pubtabnet-teds-test.git
```

Run the evaluate script
```
python evaluate.py
```

this script will evaluate the teds between
```
samples/sample_gt.html
samples/overspan_gt.html
samples/bs_pretty_gt.html
```
These three HTML files all represent the same table, and their display results in the browser are also the same.

"sample_gt.html" is the label of "PMC5755158_010_01.png" in the mini test set, but we added some html head info to improve the rendering effect.

"bs_pretty_gt.html" is the result of "sample_gt.html" formatted with the "BeautifulSoup" tool

We added "rowspan=3" to the first row and second cell of the table in "sample_gt.html" to form "overspan_gt.html"

The output of the script should be:
```
TEDS between sample_gt and sample_gt: 1.0
TEDS between sample_gt and bs_pretty_gt: 0.5661758763705194
TEDS between sample_gt and overspan_gt: 0.96
```

__The second line of output shows that the html format has a huge impact on TEDS calculations. And the reason is that the TEDS calculation tool will parse the space indentation character as part of the cell recognition result__

__The third line of output illustrates the ambiguity of using html to express the structure of the table, and it needs to be regularized before calculating TEDS.__
