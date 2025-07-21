**Example 1: 策略列表**



Input: 

```
tccli igtm DescribeStrategyList --cli-unfold-argument  \
    --InstanceId gtm-dsdd123xdo \
    --Offset 1 \
    --Limit 1 \
    --Filters.0.Name StrategyName \
    --Filters.0.Value test-strategy \
    --Filters.0.Fuzzy True
```

Output: 
```
{
    "Response": {
        "StrategySet": [
            {
                "InstanceId": "gtm-dsdd123xdo",
                "StrategyId": 1,
                "Name": "test-strategy",
                "Source": [
                    {
                        "DnsLineId": 1,
                        "Name": "默认"
                    }
                ],
                "Status": "WARN",
                "ActivePoolType": "MAIN",
                "ActiveTrafficStrategy": "WEIGHT",
                "MonitorNum": 1,
                "KeepDomainRecords": "DISABLED",
                "CreatedOn": "2020-09-22T00:00:00+00:00",
                "UpdatedOn": "2020-09-22T00:00:00+00:00"
            }
        ],
        "TotalCount": 1,
        "RequestId": "8f0325a8-4dd6-4fcb-8f6b-c45e587e51b0"
    }
}
```

