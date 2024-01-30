**Example 1: 策略列表**



Input: 

```
tccli igtm DescribeStrategyList --cli-unfold-argument  \
    --InstanceId abc \
    --Offset 1 \
    --Limit 1 \
    --Filters.0.Name abc \
    --Filters.0.Value abc \
    --Filters.0.Fuzzy True
```

Output: 
```
{
    "Response": {
        "StrategySet": [
            {
                "InstanceId": "abc",
                "StrategyId": 1,
                "Name": "abc",
                "Source": [
                    {
                        "DnsLineId": 1,
                        "Name": "abc"
                    }
                ],
                "Status": "abc",
                "ActivePoolType": "abc",
                "ActiveTrafficStrategy": "abc",
                "MonitorNum": 1,
                "KeepDomainRecords": "abc",
                "CreatedOn": "2020-09-22T00:00:00+00:00",
                "UpdatedOn": "2020-09-22T00:00:00+00:00"
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

