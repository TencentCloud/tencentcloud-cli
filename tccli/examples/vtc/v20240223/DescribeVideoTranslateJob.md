**Example 1: 调用失败示例**

调用失败示例

Input: 

```
tccli vtc DescribeVideoTranslateJob --cli-unfold-argument  \
    --JobId 111
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation.JobNotExist",
            "Message": "任务不存在。"
        },
        "RequestId": "78254ad1-c184-4e9e-b5a0-9d3fc435576b"
    }
}
```

**Example 2: 调用成功示例**

调用成功示例

Input: 

```
tccli vtc DescribeVideoTranslateJob --cli-unfold-argument  \
    --JobId vlSYvQkMM0KwPuoakawm0tPrREwc2p7c
```

Output: 
```
{
    "Response": {
        "JobErrorCode": "",
        "JobErrorMsg": "",
        "JobStatus": 7,
        "RequestId": "a974b772-3c1d-4868-8909-b1386016b9f0",
        "ResultVideoUrl": "http://xxx.com/url/xxx.mp4",
        "TranslateResults": [
            {
                "SourceText": "当工作或学习结果不理想，",
                "TargetText": "When the result of work or study is not ideal"
            },
            {
                "SourceText": "甚至面临被全盘否定的情况时，",
                "TargetText": "Even when faced with the situation of being completely denied"
            },
            {
                "SourceText": "你会如何应对？",
                "TargetText": "How would you respond?"
            },
            {
                "SourceText": "可以举例说明当时你是如何处理负面情绪，",
                "TargetText": "You can give an example of how you dealt with negative emotions at that time."
            },
            {
                "SourceText": "并找到解决办法的。",
                "TargetText": "And find a solution."
            }
        ]
    }
}
```

