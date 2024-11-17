**Example 1: 指定IPV6转换实例查询**

指定IPV6转换实例查询

Input: 

```
tccli vpc DescribeIp6Translators --cli-unfold-argument  \
    --Ip6TranslatorIds ip6-mhnrv51i
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Ip6TranslatorSet": [
            {
                "Ip6TranslatorId": "ip6-mhnrv51i",
                "Ip6TranslatorName": "ukiotest1",
                "Vip6": "2402:4e00:40:40::2:2a6",
                "IspName": "BGP",
                "TranslatorStatus": "RUNNING",
                "CreatedTime": "2023-07-13T11:12:06Z",
                "Ip6RuleCount": 1,
                "IP6RuleSet": [
                    {
                        "Ip6RuleId": "rule6-ganlwp48",
                        "Ip6RuleName": "未命名",
                        "Vip6": "2402:4e00:40:40::2:2a6",
                        "Vport6": 80,
                        "Protocol": "TCP",
                        "Vip": "10.0.0.0",
                        "Vport": 80,
                        "RuleStatus": "RUNNING",
                        "CreatedTime": "2023-07-26T02:27:16Z"
                    }
                ]
            }
        ],
        "RequestId": "c5ad87da-28fb-4f5d-8fce-bf19a06cfe6d"
    }
}
```

**Example 2: 指定Filters查询IPV6转换实例**

指定Filters查询IPV6转换实例

Input: 

```
tccli vpc DescribeIp6Translators --cli-unfold-argument  \
    --Filters.0.Name ip6-translator-vip6 \
    --Filters.0.Values 2402:4e00:40:40::2:2a6
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Ip6TranslatorSet": [
            {
                "Ip6TranslatorId": "ip6-mhnrv51i",
                "Ip6TranslatorName": "ukiotest1",
                "Vip6": "2402:4e00:40:40::2:2a6",
                "IspName": "BGP",
                "TranslatorStatus": "RUNNING",
                "CreatedTime": "2023-07-13T11:12:06Z",
                "Ip6RuleCount": 1,
                "IP6RuleSet": [
                    {
                        "Ip6RuleId": "rule6-ganlwp48",
                        "Ip6RuleName": "未命名",
                        "Vip6": "2402:4e00:40:40::2:2a6",
                        "Vport6": 80,
                        "Protocol": "TCP",
                        "Vip": "10.0.0.0",
                        "Vport": 80,
                        "RuleStatus": "RUNNING",
                        "CreatedTime": "2023-07-26T02:27:16Z"
                    }
                ]
            }
        ],
        "RequestId": "c5ad87da-28fb-4f5d-8fce-bf19a06cfe6d"
    }
}
```

