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
        "RequestId": "xx",
        "UnhandleMediumLevelEventCount": 1
    }
}
```

