**Example 1: 指定IPV6转换实例查询**

指定IPV6转换实例查询

Input: 

```
tccli vpc DescribeIp6Translators --cli-unfold-argument  \
    --Ip6TranslatorIds abc \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --Offset 0 \
    --Limit 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Ip6TranslatorSet": [
            {
                "Ip6TranslatorId": "abc",
                "Ip6TranslatorName": "abc",
                "Vip6": "abc",
                "IspName": "abc",
                "TranslatorStatus": "abc",
                "CreatedTime": "2020-09-22T00:00:00+00:00",
                "Ip6RuleCount": 0,
                "IP6RuleSet": [
                    {
                        "Ip6RuleId": "abc",
                        "Ip6RuleName": "abc",
                        "Vip6": "abc",
                        "Vport6": 0,
                        "Protocol": "abc",
                        "Vip": "abc",
                        "Vport": 0,
                        "RuleStatus": "abc",
                        "CreatedTime": "2020-09-22T00:00:00+00:00"
                    }
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

**Example 2: 指定Filters查询IPV6转换实例**

指定Filters查询IPV6转换实例

Input: 

```
tccli vpc DescribeIp6Translators --cli-unfold-argument  \
    --Ip6TranslatorIds abc \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --Offset 0 \
    --Limit 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Ip6TranslatorSet": [
            {
                "Ip6TranslatorId": "abc",
                "Ip6TranslatorName": "abc",
                "Vip6": "abc",
                "IspName": "abc",
                "TranslatorStatus": "abc",
                "CreatedTime": "2020-09-22T00:00:00+00:00",
                "Ip6RuleCount": 0,
                "IP6RuleSet": [
                    {
                        "Ip6RuleId": "abc",
                        "Ip6RuleName": "abc",
                        "Vip6": "abc",
                        "Vport6": 0,
                        "Protocol": "abc",
                        "Vip": "abc",
                        "Vport": 0,
                        "RuleStatus": "abc",
                        "CreatedTime": "2020-09-22T00:00:00+00:00"
                    }
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

