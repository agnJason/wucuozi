## 简介

本代码实现了针对毕业论文文档的错别字检查功能，主要利用了[pycorrector](https://github.com/shibing624/pycorrector)自然语言处理库。

## 环境

准备一个python3.8的环境

```shell
pip install -r requirements.txt
```

测试环境，如果通过，会自动开始下载权重文件，下载完输出正确句子和错误位置

```
python -c "import pycorrector;print(pycorrector.correct('我是浙江打学的学生'))"
```

此时，如果出现以下报错

```
ImportError: pycorrector dependencies are not fully installed, they are required for statistical language model.Please use "pip install kenlm" to install it.if you are Win, Please install kenlm in cgwin.
```

使用一下代码安装kenlm,安装后重新测试环境

```
pip install https://github.com/kpu/kenlm/archive/master.zip
```

## 使用

可以对样例.docx检查错别字

```shell
python wucuozi.py
```

output:

```python
=========开始检查错别字=========
在第0段3个位置发现错别字！错别字为“偏”，应改为“篇”
在第1段5个位置发现错别字！错别字为“提”，应改为“题”
在第2段5个位置发现错别字！错别字为“设”，应改为“社”
在第2段22个位置发现错别字！错别字为“材”，应改为“财”
在第2段47个位置发现错别字！错别字为“衣”，应改为“依”
在第2段83个位置发现错别字！错别字为“滤”，应改为“虑”
在第2段107个位置发现错别字！错别字为“成”，应改为“城”
=========以下为修正后文字=========
这是一篇论文
这是一个标题
近日，新华社记者就房地产税改各试点问题采访了财政部有关负责人。有关负责人表示，房地产税改革试点依照全国人大常委会的授全进行，一些城市开展了调查摸底和初步研究，但综合考虑各方面的情况，今年内不具备扩大房地产税改革试点城市的条件。
```

也可以将要检测的docx的路径传入

```
python .\wucuozi.py xx.docx
```



