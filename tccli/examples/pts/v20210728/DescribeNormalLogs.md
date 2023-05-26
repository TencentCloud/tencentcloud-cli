**Example 1: 查询压测过程日志**

查询压测过程日志

Input: 

```
tccli pts DescribeNormalLogs --cli-unfold-argument  \
    --ProjectId project-fjs583kq \
    --ScenarioId scenario-q63bkqsa \
    --JobId job-657v4tmi \
    --LogType console
```

Output: 
```
{
    "Response": {
        "Context": "123-456-789",
        "NormalLogs": [],
        "RequestId": "nes5mdwkfrbfhbpjrs4ox6ck41xjn9jp"
    }
}
```

