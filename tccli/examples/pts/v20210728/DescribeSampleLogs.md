**Example 1: 查询采样日志**

查询采样日志

Input: 

```
tccli pts DescribeSampleLogs --cli-unfold-argument  \
    --ProjectId project-fjs583kq \
    --ScenarioId scenario-q63bkqsa \
    --JobId job-657v4tmi \
    --LogType request
```

Output: 
```
{
    "Response": {
        "RequestId": "85f22814-36b9-44e0-bfaa-18fad9accaf8",
        "Total": 10,
        "Context": "12353-2432423",
        "SampleLogs": []
    }
}
```

