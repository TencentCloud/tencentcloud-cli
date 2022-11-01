**Example 1: 查询待处理安全事件**



Input: 

```
tccli tcss DescribeContainerSecEventSummary --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "UnhandledFileCnt": 1,
        "UnhandledEscapeCnt": 1,
        "UnhandledRiskSyscallCnt": 1,
        "RequestId": "xx",
        "UnhandledReverseShellCnt": 1,
        "UnhandledAbnormalProcessCnt": 1,
        "UnhandledVirusEventCnt": 1,
        "UnhandledMaliciousConnectionEventCnt": 1,
        "UnhandledK8sApiEventCnt": 1
    }
}
```

