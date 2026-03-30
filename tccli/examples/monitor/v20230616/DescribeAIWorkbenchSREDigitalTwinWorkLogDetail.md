**Example 1: 成功**



Input: 

```
tccli monitor DescribeAIWorkbenchSREDigitalTwinWorkLogDetail --cli-unfold-argument  \
    --WorkLogID 2
```

Output: 
```
{
    "Response": {
        "Data": {
            "Content": "https://xxx-12345.cos.ap-guangzhou.myqcloud.com/report/12345/xxx",
            "TaskType": "custom",
            "DialogID": 1341
        },
        "JSONStrPaths": [],
        "RequestId": "4f3491c3-8c4f-4597-b2b6-3c88044a2a60"
    }
}
```

