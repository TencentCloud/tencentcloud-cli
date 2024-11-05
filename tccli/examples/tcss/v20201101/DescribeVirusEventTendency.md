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
                "EventCount": 1,
                "IsolateEventCount": 1
            }
        ],
        "RequestId": "29b37d86-f63d-43d1-b21a-640e82965198"
    }
}
```

