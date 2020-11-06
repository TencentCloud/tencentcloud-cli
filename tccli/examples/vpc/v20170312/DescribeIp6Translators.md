**Example 1: 指定IPV6转换实例查询**

指定IPV6转换实例查询

Input: 

```
tccli vpc DescribeIp6Translators --cli-unfold-argument  \
    --Ip6TranslatorId ip6-90pt7p9q
```

Output: 
```
{
    "Response": {
        "TotalCount": 3,
        "Ip6TranslatorSet": [
            {
                "Ip6TranslatorId": "ip6-ml2hm2dg",
                "Ip6TranslatorName": "未命名",
                "Vip6": null,
                "IspName": "",
                "TranslatorStatus": "CREATING",
                "CreatedTime": "2019-01-10T06:05:37Z",
                "Ip6RuleCount": 0,
                "Ip6RuleSet": []
            },
            {
                "Ip6TranslatorId": "ip6-90pt7p9q",
                "Ip6TranslatorName": "kkkk",
                "Vip6": "2402:4e00:20:100::2:1011",
                "IspName": "",
                "TranslatorStatus": "RUNNING",
                "CreatedTime": "2019-01-10T01:33:32Z",
                "Ip6RuleCount": 5,
                "Ip6RuleSet": [
                    {
                        "Ip6RuleId": "rule6-c1rvcaoa",
                        "Ip6RuleName": "未命名",
                        "Vip6": "2402:4e00:20:100::2:1011",
                        "Vport6": 0,
                        "Protocol": "tcp",
                        "Vip": "",
                        "Vport": 0,
                        "RuleStatus": "CREATING",
                        "CreatedTime": "2019-01-10T04:26:38Z"
                    },
                    {
                        "Ip6RuleId": "rule6-r92oxfhm",
                        "Ip6RuleName": "未命名",
                        "Vip6": "2402:4e00:20:100::2:1011",
                        "Vport6": 1,
                        "Protocol": "tcp",
                        "Vip": "100.100.1.1",
                        "Vport": 2,
                        "RuleStatus": "RUNNING",
                        "CreatedTime": "2019-01-10T07:59:02Z"
                    },
                    {
                        "Ip6RuleId": "rule6-kxlgqufa",
                        "Ip6RuleName": "未命名",
                        "Vip6": "2402:4e00:20:100::2:1011",
                        "Vport6": 0,
                        "Protocol": "tcp",
                        "Vip": "",
                        "Vport": 0,
                        "RuleStatus": "CREATING",
                        "CreatedTime": "2019-01-10T07:59:02Z"
                    },
                    {
                        "Ip6RuleId": "rule6-k5l5hnwk",
                        "Ip6RuleName": "未命名",
                        "Vip6": "2402:4e00:20:100::2:1011",
                        "Vport6": 0,
                        "Protocol": "tcp",
                        "Vip": "",
                        "Vport": 0,
                        "RuleStatus": "CREATING",
                        "CreatedTime": "2019-01-10T08:12:27Z"
                    },
                    {
                        "Ip6RuleId": "rule6-7v3vwgec",
                        "Ip6RuleName": "未命名",
                        "Vip6": "2402:4e00:20:100::2:1011",
                        "Vport6": 0,
                        "Protocol": "tcp",
                        "Vip": "",
                        "Vport": 0,
                        "RuleStatus": "CREATING",
                        "CreatedTime": "2019-01-10T08:12:27Z"
                    }
                ]
            },
            {
                "Ip6TranslatorId": "ip6-8svxwtts",
                "Ip6TranslatorName": "未命名",
                "Vip6": null,
                "IspName": "",
                "TranslatorStatus": "CREATING",
                "CreatedTime": "2019-01-09T13:50:06Z",
                "Ip6RuleCount": 0,
                "Ip6RuleSet": []
            }
        ],
        "RequestId": "fb44e0a1-1827-4d3d-abde-9514e884dbeb"
    }
}
```

**Example 2: 指定Filters查询IPV6转换实例**

指定Filters查询IPV6转换实例

Input: 

```
tccli vpc DescribeIp6Translators --cli-unfold-argument  \
    --Filters.0.Name ip6-translator-uid \
    --Filters.0.Values ip6-8svxwtts
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Ip6TranslatorSet": [
            {
                "Ip6TranslatorId": "ip6-8svxwtts",
                "Ip6TranslatorName": "未命名",
                "Vip6": null,
                "IspName": "",
                "TranslatorStatus": "CREATING",
                "CreatedTime": "2019-01-09T13:50:06Z",
                "Ip6RuleCount": 0,
                "Ip6RuleSet": []
            }
        ],
        "RequestId": "cbf8a954-d135-4b52-9935-89e9ec88b536"
    }
}
```

