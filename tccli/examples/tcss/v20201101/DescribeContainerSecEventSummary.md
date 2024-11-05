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
        "RequestId": "8a64a4f9-864c-49c6-adcb-21b483de477a",
        "UnhandledReverseShellCnt": 1,
        "UnhandledAbnormalProcessCnt": 1,
        "UnhandledVirusEventCnt": 1,
        "UnhandledMaliciousConnectionEventCnt": 1,
        "UnhandledK8sApiEventCnt": 1
    }
}
```

