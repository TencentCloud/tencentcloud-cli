**Example 1: 策略详情**



Input: 

```
tccli igtm DescribeStrategyDetail --cli-unfold-argument  \
    --InstanceId abc \
    --StrategyId 0
```

Output: 
```
{
    "Response": {
        "StrategyDetail": {
            "InstanceId": "abc",
            "StrategyId": 1,
            "Name": "abc",
            "Source": [
                {
                    "DnsLineId": 1,
                    "Name": "abc"
                }
            ],
            "MainAddressPoolSet": [
                {
                    "MainAddressPoolId": 1,
                    "AddressPools": [
                        {
                            "PoolId": 1,
                            "Weight": 1
                        }
                    ],
                    "MinSurviveNum": 1,
                    "TrafficStrategy": "abc"
                }
            ],
            "FallbackAddressPoolSet": [
                {
                    "MainAddressPoolId": 1,
                    "AddressPools": [
                        {
                            "PoolId": 1,
                            "Weight": 1
                        }
                    ],
                    "MinSurviveNum": 1,
                    "TrafficStrategy": "abc"
                }
            ],
            "KeepDomainRecords": "abc"
        },
        "RequestId": "abc"
    }
}
```

