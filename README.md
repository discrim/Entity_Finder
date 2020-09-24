# Entity_Finder
## Logistics
- Affiliation: University of Michigan - Ann Arbor
- Term: 2020 Fall
- Course: EECS 595 Natural Language Processing
- Note: HW1
## Usage
```python
import namedentity
in1 = "Today is September 23, 2020. I have one hundred dollars in my pocket. I am going to buy a nice jersey from www.fancyclothes.com with this money."
print(namedentity.ner(in1))
```
```
DATE is DATE. I have DOLLAR_AMOUNT in my pocket. I am going to buy a nice jersey from WEB_ADDRESS with this money.
```
## Problem Statement
This is a practice ground for text processing using regular expressions. Some textual strings may have specific semantic meanings such as `PERSON NAME`, `LOCATION NAME`, `ORGANIZATION NAME`, `TIME`, `DATE`, `EMAIL ADDRESS`, `WEB ADDRESS`, `DOLLAR AMOUNT`, etc. This code specifies the following named entites: `TIME`, `DATE`, `EMAIL ADDRESS`, `WEB ADDRESS`, `DOLLAR AMOUNT` and replaces them with the predefined placeholders. Since each entity can be written in various formats, I tried to cover as many forms as possible, but still there will be false positive and false negative cases.
## Potential Issues
### Time
I included expressions to detect 'five past ten' form of time. There are also some expressions to find 'five to ten'. However, this 'some number to some number' can be also used other than time description such as "My score ranges from five to ten". These kind of phrases will be false positive for the detection.
### Date
It can find seven days of the week, number-only dates, English month + number days and years. However, it cannot find dates with lots of English such as 'five days ago'.
### Email Address
Since all email address is a concatenation of (some string without spacebar) + 'at' symbol + (some string without spacebar) so it can be easily found with simple regular expression.
### Web Address
I wrote regular expressions to match one of the three things: Beginning with 'www.', beginning with 'http://' or 'https://', and ending with all of the top-level domains (e.g. '.com', '.net') listed on Wikipedia. If someone creates a new address that does not start with 'www.' or 'http://' or 'https://', and does not finish with top-level domains in that list, my regex cannot find it. An arbitrary example is 'i-am-not-going-to-be.caught'.
### Dollar Amount
If there is a cent-only string such as 'one cent' ~ 'ninety nine cents', it cannot detect the string.
