**Example 1: 正常响应**



Input: 

```
tccli tdmq DescribeRocketMQPublicAccessMonitorData --cli-unfold-argument  \
    --InstanceId rocketmq-a52qova7x97b \
    --StartTime 2024-12-04T15:06:49+08:00 \
    --EndTime 2024-12-04T16:06:49+08:00 \
    --Period 60 \
    --MetricName RocketmqPublicNetworkIntrafficVipRatio
```

Output: 
```
{
    "Response": {
        "StartTime": "2024-12-04T15:06:00+08:00",
        "EndTime": "2024-12-04T16:06:00+08:00",
        "Period": 60,
        "MetricName": "RocketmqPublicNetworkIntrafficVipRatio",
        "DataPoints": [
            {
                "Timestamps": [
                    1733295960,
                    1733296020,
                    1733296080,
                    1733296140,
                    1733296200,
                    1733296260,
                    1733296320,
                    1733296380,
                    1733296440,
                    1733296500,
                    1733296560,
                    1733296620,
                    1733296680,
                    1733296740,
                    1733296800,
                    1733296860,
                    1733296920,
                    1733296980,
                    1733297040,
                    1733297100,
                    1733297160,
                    1733297220,
                    1733297280,
                    1733297340,
                    1733297400,
                    1733297460,
                    1733297520,
                    1733297580,
                    1733297640,
                    1733297700,
                    1733297760,
                    1733297820,
                    1733297880,
                    1733297940,
                    1733298000,
                    1733298060,
                    1733298120,
                    1733298180,
                    1733298240,
                    1733298300,
                    1733298360,
                    1733298420,
                    1733298480,
                    1733298540,
                    1733298600,
                    1733298660,
                    1733298720,
                    1733298780,
                    1733298840,
                    1733298900,
                    1733298960,
                    1733299020,
                    1733299080,
                    1733299140,
                    1733299200,
                    1733299260
                ],
                "Values": [
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0
                ]
            }
        ],
        "RequestId": "a6ebee33-5790-435a-a204-dda200d360af",
        "Msg": ""
    }
}
```

