# how-to-diy-smart-speaker

How to DIY a Chinese Smart Speaker

Sphinx 生成 
---

打开 [http://www.speech.cs.cmu.edu/tools/lmtool-new.html](http://www.speech.cs.cmu.edu/tools/lmtool-new.html)

 1. 点击 Choose File 上传文件
 2. 点击 COMPILE KNOWLEDGE BASE 进行转换
 3. 打开 [http://www.speech.cs.cmu.edu/tools/product/1503889661_19829/](http://www.speech.cs.cmu.edu/tools/product/1503889661_19829/) 下载 tgz 文件


````
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
INFO:mic:Use ReSpeaker MicArray UAC2.0: USB Audio (hw:2,0)

INFO:mic:Start detecting
INFO:mic:Detected 空调
INFO:mic:Detected 空调
INFO:mic:Detected 度
INFO:mic:Detected 今天
INFO:mic:Detected 今天
INFO:mic:Detected 空调
```

下载的 txt 需要生成模型

执行:

```
cd sphinx-models
python create_symbol.py 
```
 
###  Mac OS

```
brew install portaudio hidapi
```
 

```
python assistant.py                                                                             22:48:35
ERROR:root:cython-hidapi is required on a Mac OS X Machine
```


```
pip install cython
git clone https://github.com/gbishop/cython-hidapi.git
python setup.py install
```

Text Generate ?
---


