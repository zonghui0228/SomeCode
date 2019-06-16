# *_* coding: utf-8 *_*
# @Time     : 11/26/2018 11:05 AM
# @Author   : zong hui

# parse the result of metamap.
# convert to a list. contained Phrase, Metamap_CUI, Semantic_Type, MetaMap_Word , Raw_Word

import re
import os
import csv


def single_parse(infile, semantic_type = None):
    """
    Description: parse single MetaMap results file.
    Usage: t = single_parse("./example_data/24157031.txt")
    :param infile: the result file by tools-MetaMap.
    :param semantic_type: the concepts you want to extract.
    :return: concept terms
    """
    # print "Parsing file: {}".format(infile)
    terms = []  # all terms
    filename = os.path.split(infile)[1].split('.')[0]
    with open(infile, 'r') as f:
        for line in f:
            # print line
            line = line.strip()
            if line.startswith("Phrase"):
                Phrase = line.strip()
            else:
                CUI = re.compile(r"\d+   C\d+:").findall(line)
                if CUI:
                    MetaMap_CUI = CUI[0][CUI[0].index("C"):-1]
                    # Semantic type
                    if re.compile(r"\[([^\[]+)\]$").findall(line):
                        Semantic_Type = re.compile(r"\[([^\[]+)\]$").findall(line)[0]
                    else:
                        Semantic_Type = ""
                    # MetaMap Word
                    if re.compile(r" \(.+\) \[").findall(line):
                        MetaMap_Word = re.compile(r" \(.+\) \[").findall(line)[0][2:-3]
                    else:
                        MetaMap_Word = ""
                    # raw word
                    # Raw_Word = re.compile(r":.+\[").findall(line)[0][1:-1].split(" (")[0]
                    Raw_Word = line.replace("["+Semantic_Type+"]", "").replace(" ("+MetaMap_Word+") ", "")
                    Raw_Word = re.sub(r"\d+   C\d+:", "", Raw_Word)
                    Semantic_Type_mul = [s.replace("@", ", ") for s in Semantic_Type.replace(", ", "@").split(",")]
                    for Sem_type in Semantic_Type_mul:
                        term = [filename, MetaMap_CUI, Sem_type, MetaMap_Word, Raw_Word, Phrase]
                        terms.append(term)
                else:
                    pass
    if semantic_type:
        new_terms = [t for t in terms if t[2] == semantic_type]
        return new_terms
    return terms


def batch_parse(infolder, semantic_type = None):
    """
    Description: parse batch file
    Usage: batch_parse("./example_data/")
    :param infolder:
    :param semantic_type:
    :return:
    """
    files = os.listdir(infolder)
    filecounts = len(files)
    print("there are {} files need to be parsed".format(filecounts))
    all_terms = []
    n = 0
    for file in files:
        n += 1
        if n % 100 == 0: print("parsing {}/{}".format(n, filecounts))
        filepath = os.path.join(infolder, file)
        terms = single_parse(filepath, semantic_type)
        all_terms.extend(terms)
    print("there are {} files have been parsed.".format(len(files)))
    print("there are {} MetaMap terms found.".format(len(all_terms)))
    return all_terms

def OutputTerms(terms, outfile, specialCUI = None):
    """
    Description: write MetaMap terms to file.
    :param terms: MetaMap concepts from the MetaMap results.
    :param outfile: the file for output terms.
    :param specialCUI: if output special concepts, please use, or default.
    :return: nothing.
    """
    with open(outfile, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(["filename", "CUI", "semantic type", "MetaMap word", "raw word", "phrase"])
        n = 0
        for term in terms:
            if specialCUI:
                if isinstance(specialCUI, list):
                    if term[1] in specialCUI:
                        n += 1
                        writer.writerow(term)
                else:
                    print("specialCUI should be a list")
                    return 'done!'
            else:
                n += 1
                writer.writerow(term)
    print("finshed! processed {} terms, output {} terms.".format(len(terms), n))
    return 'done!'


if __name__ == "__main__":
    # single file
    terms = single_parse("./example_data/24157031.txt")
    for t in terms:
        print(t)
    # batch process
    terms = batch_parse("./example_data/")
    for t in terms:
        print(t)


    print("done!")


