**Example 1: DescribeAsrHotwords**



Input: 

```
tccli mps DescribeAsrHotwords --cli-unfold-argument  \
    --HotwordsId hwd-aexxxxxxxxxxxxxx1481
```

Output: 
```
{
    "Response": {
        "Content": "腾讯云|10,语音识别|5,ASR|10",
        "CreateTime": "2025-03-19T03:29:06Z",
        "FileName": "",
        "HotWords": [
            {
                "Id": 1,
                "Text": "腾讯云",
                "Weight": 10
            },
            {
                "Id": 2,
                "Text": "语音识别",
                "Weight": 5
            },
            {
                "Id": 3,
                "Text": "ASR",
                "Weight": 10
            }
        ],
        "HotwordsId": "hwd-aexxxxxxxxxxxxxx1481",
        "Limit": 0,
        "Name": "HotwordsNameExample",
        "Offset": 0,
        "RequestId": "bad606d3-8a49-427f-a6a6-26c9f1fe1dc3",
        "Status": 0,
        "Type": 0,
        "UpdateTime": "2025-03-19T03:29:06Z",
        "WordCount": 3
    }
}
```

