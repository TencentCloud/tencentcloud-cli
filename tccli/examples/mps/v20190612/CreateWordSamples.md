**Example 1: 创建关键词素材-All**

Usages=All，则该关键词可用于通过 OCR 技术、ASR 技术，进行内容识别、不适宜内容识别。

Input: 

```
tccli mps CreateWordSamples --cli-unfold-argument  \
    --Usages All \
    --Words.0.Keyword 网红 \
    --Words.0.Tags 娱乐
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

**Example 2: 创建关键词素材-Review**

Usages=Review，则该关键词可用于通过 OCR 技术、ASR 技术，进行不适宜内容识别。

Input: 

```
tccli mps CreateWordSamples --cli-unfold-argument  \
    --Usages Review \
    --Words.0.Keyword 张三 \
    --Words.0.Tags 政治
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

**Example 3: 创建关键词素材-Recognition**

Usages=["Recognition.Ocr","Review.Ocr"]，则该关键词可用于通过 OCR 技术，进行内容识别、不适宜内容识别。

Input: 

```
tccli mps CreateWordSamples --cli-unfold-argument  \
    --Usages Recognition.Ocr Review.Ocr \
    --Words.0.Keyword 网红 \
    --Words.0.Tags 娱乐
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

