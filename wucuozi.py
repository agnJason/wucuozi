import sys
from docx import Document
from pycorrector.macbert.macbert_corrector import MacBertCorrector

m = MacBertCorrector("shibing624/macbert4csc-base-chinese")

if len(sys.argv)>1:
    doc_name = sys.argv[1]
else:
    doc_name = '样例.docx'
doc = Document(doc_name)

corrs = []
errors = []
print("=========开始检查错别字=========")
#每一段的内容
for i, para in enumerate(doc.paragraphs):
    corr, error = m.macbert_correct(para.text.split()[0])
    corrs.append(corr)
    errors.append(error)
    for e in error:
        print("在第{}段{}个位置发现错别字！错别字为“{}”，应改为“{}”".format(i, e[2], e[0], e[1]))
print("=========以下为修正后文字=========")
for c in corrs:
    print(c)