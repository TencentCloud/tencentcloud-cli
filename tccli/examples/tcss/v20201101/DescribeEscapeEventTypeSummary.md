**Example 1: 统计容器逃逸各事件类型和待处理事件数**



Input: 

```
tccli tcss DescribeEscapeEventTypeSummary --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RiskContainerEventCount": 0,
        "ProcessPrivilegeEventCount": 0,
        "ContainerEscapeEventCount": 0,
        "RequestId": "xx",
        "PendingEscapeEventCount": 0
    }
}
```

