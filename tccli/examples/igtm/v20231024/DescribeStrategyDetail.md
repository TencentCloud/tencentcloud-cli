**Example 1: 策略详情**



Input: 

```
tccli igtm DescribeStrategyDetail --cli-unfold-argument  \
    --InstanceId gtm-dsdd123xdo \
    --StrategyId 1
```

Output: 
```
{
    "Response": {
        "StrategyDetail": {
            "InstanceId": "gtm-dsdd123xdo",
            "StrategyId": 1,
            "Name": "测试策略",
            "Source": [
                {
                    "DnsLineId": 1,
                    "Name": "默认"
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
                    "TrafficStrategy": "WEIGHT"
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
                    "TrafficStrategy": "WEIGHT"
                }
            ],
            "KeepDomainRecords": "DISABLED",
            "CreatedOn": "2020-09-22T00:00:00+00:00",
            "UpdatedOn": "2020-09-22T00:00:00+00:00"
        },
        "RequestId": "8f0325a8-4dd6-4fcb-8f6b-c45e587e51b0"
    }
}
```

