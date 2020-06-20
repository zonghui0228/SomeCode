# MetaMap Result Parser
A script to extract UMLS semantic types from results of MetaMap .

#### related website
* [UMLS](https://www.nlm.nih.gov/research/umls/), Unified Medical Language System
* [MetaMap](https://metamap.nlm.nih.gov/), A Tool For Recognizing UMLS Concepts in Text

## Usage
```python
import MetaMapResParser
```

```python
# process single file
MetaMapResParser.single_parse("./example_data/24157031.txt")
```

```python
# constraints on semantic types
MetaMapResParser.single_parse("./example_data/24157031.txt", semantic_type = 'Temporal Concept')
```

```python
# batch process
MetaMapResParser.batch_parse("./example_data/")
```