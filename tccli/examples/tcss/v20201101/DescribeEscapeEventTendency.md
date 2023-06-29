**Example 1: 查询待处理逃逸事件趋势**



Input: 

```
tccli tcss DescribeEscapeEventTendency --cli-unfold-argument  \
    --EndTime 2021-05-01 \
    --StartTime 2021-05-07
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Date": "2020-09-22",
                "ContainerEscapeEventCount": 0,
                "ProcessPrivilegeEventCount": 0,
                "RiskContainerEventCount": 0
            }
        ],
        "RequestId": "xx"
    }
}
```

