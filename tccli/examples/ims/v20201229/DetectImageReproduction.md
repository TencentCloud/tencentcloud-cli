**Example 1: 图片翻拍检测**

识别图片是否为翻拍图片，返回图片的判定类别和置信度。目前支持二维码翻拍和陈列翻拍的识别；

Input: 

```
tccli ims DetectImageReproduction --cli-unfold-argument  \
    --ImageBase64 picture base64 data
```

Output: 
```
{
    "Response": {
        "RequestId": "asdasd",
        "Results": [
            {
                "Label": 1,
                "Confidence": 0.9578
            }
        ]
    }
}
```

