**Example 1: 获取图片的下载地址**



Input: 

```
tccli ape BatchDescribeOrderImage --cli-unfold-argument  \
    --OrderIds apod-bt0i48tz
```

Output: 
```
{
    "Response": {
        "RequestId": "s1589773775497713697",
        "ImageUrls": [
            "http://demo.jpg"
        ]
    }
}
```

