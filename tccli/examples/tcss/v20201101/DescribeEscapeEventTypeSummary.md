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
        "RequestId": "29b37d86-f63d-43d1-b21a-640e82965198",
        "PendingEscapeEventCount": 0
    }
}
```

