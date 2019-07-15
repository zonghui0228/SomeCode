# MetaMap-ResultParser
A script to process MetaMap results.

#### related website
* [UMLS](https://www.nlm.nih.gov/research/umls/), Unified Medical Language System
* [MetaMap](https://metamap.nlm.nih.gov/), A Tool For Recognizing UMLS Concepts in Text

## Usage
        import MetaMapResParser
        
        # process single file
        MetaMapResParser.single_parse("./example_data/24157031.txt")
        
        # constraints on semantic types
        MetaMapResParser.single_parse("./example_data/24157031.txt", semantic_type = 'Temporal Concept')
        
        # batch process
        MetaMapResParser.batch_parse("./example_data/")
