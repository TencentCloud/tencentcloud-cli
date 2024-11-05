**Example 1: 查询k8sapi异常事件统计**



Input: 

```
tccli tcss DescribeK8sApiAbnormalSummary --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "UnhandleEventCount": 1,
        "UnhandleHighLevelEventCount": 1,
        "UnhandleNoticeLevelEventCount": 1,
        "UnhandleLowLevelEventCount": 1,
        "RequestId": "29b37d86-f63d-43d1-b21a-640e82965198",
        "UnhandleMediumLevelEventCount": 1
    }
}
```

