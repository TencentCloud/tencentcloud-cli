**Example 1: 调用失败示例**



Input: 

```
tccli tiia DetectEnvelope --cli-unfold-argument  \
    --ImageUrl https://test.jpg
```

Output: 
```
{
    "Response": {
        "RequestId": "ad418ac5-fbfd-4bd7-8f4a-35ab085e27dd"
    }
}
```

**Example 2: 调用成功示例**



Input: 

```
tccli tiia DetectEnvelope --cli-unfold-argument  \
    --ImageUrl http://test.jpg
```

Output: 
```
{
    "Response": {
        "FirstTags": [
            {
                "Name": "非文件封",
                "Confidence": 97.76
            },
            {
                "Name": "文件封",
                "Confidence": 2.24
            }
        ],
        "SecondTags": [
            {
                "Name": "非文件封",
                "Confidence": 97.5
            },
            {
                "Name": "非顺丰文件封正面",
                "Confidence": 2.28
            },
            {
                "Name": "顺丰文件封正面",
                "Confidence": 0.09
            },
            {
                "Name": "非顺丰文件封反面",
                "Confidence": 0.07
            },
            {
                "Name": "顺丰文件封反面",
                "Confidence": 0.05
            }
        ],
        "RequestId": "c7552894-0e1c-468d-afc7-685483c3e3be"
    }
}
```

