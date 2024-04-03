**Example 1: 安全属性识别请求失败**

安全属性识别请求失败

Input: 

```
tccli tiia DetectSecurity --cli-unfold-argument  \
    --ImageUrl https://123.jpg
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation.DownLoadError",
            "Message": "下载失败"
        },
        "RequestId": "a169390a-6ff3-4c42-ad25-a7858c35e516"
    }
}
```

**Example 2: 安全属性识别请求成功**

安全属性识别请求成功

Input: 

```
tccli tiia DetectSecurity --cli-unfold-argument  \
    --ImageUrl https://test.jpg
```

Output: 
```
{
    "Response": {
        "Bodies": [
            {
                "Attributes": [
                    {
                        "Confidence": 0.9608861,
                        "Label": "无安全帽",
                        "Name": "安全帽识别"
                    },
                    {
                        "Confidence": 0.9768763,
                        "Label": "没有电话",
                        "Name": "玩手机识别"
                    },
                    {
                        "Confidence": 0.8206851,
                        "Label": "没有抽烟",
                        "Name": "抽烟识别"
                    },
                    {
                        "Confidence": 0,
                        "Label": "被优选过滤",
                        "Name": "口罩识别"
                    },
                    {
                        "Confidence": 0.9113377,
                        "Label": "无工地安全带",
                        "Name": "工地安全带识别"
                    },
                    {
                        "Confidence": 0.7201198,
                        "Label": "无手套",
                        "Name": "手套识别"
                    },
                    {
                        "Confidence": 0.6875998,
                        "Label": "无工服",
                        "Name": "工服识别"
                    },
                    {
                        "Confidence": 0.611658,
                        "Label": "无护目镜",
                        "Name": "护目镜识别"
                    },
                    {
                        "Confidence": 0.9828068,
                        "Label": "无反光衣",
                        "Name": "反光衣识别"
                    }
                ],
                "DetectConfidence": 0.914,
                "Rect": {
                    "Height": 1110,
                    "Width": 440,
                    "X": 217,
                    "Y": 79
                }
            }
        ],
        "RequestId": "8a3f48ea-f995-4ad2-9ff5-7f8faf8bdbaf"
    }
}
```

