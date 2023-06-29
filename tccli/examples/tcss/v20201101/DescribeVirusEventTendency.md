**Example 1: 运行时木马趋势数据获取**



Input: 

```
tccli tcss DescribeVirusEventTendency --cli-unfold-argument  \
    --TendencyPeriod 7
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Date": "2020-09-22",
                "PendingEventCount": 1,
                "RiskContainerCount": 1,
                "EventCount": 1
            }
        ],
        "RequestId": "xx"
    }
}
```

