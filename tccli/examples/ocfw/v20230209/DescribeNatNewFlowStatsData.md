**Example 1: NAT监控面板-峰值均值带宽统计**



Input: 

```
tccli ocfw DescribeNatNewFlowStatsData --cli-unfold-argument  \
    --TimeType 0 \
    --NatInstanceId abc
```

Output: 
```
{
    "Response": {
        "InputTrendData": [
            {
                "Label": "abc",
                "Value": 0,
                "Name": "abc"
            }
        ],
        "OutputTrendData": [
            {
                "Label": "abc",
                "Value": 0,
                "Name": "abc"
            }
        ],
        "InputMax": 0,
        "OutputMax": 0,
        "InputPercent": 0,
        "OutputPercent": 0,
        "RequestId": "abc"
    }
}
```

