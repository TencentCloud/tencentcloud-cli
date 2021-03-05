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
                "Ip6RuleCount": 0
            },
            {
                "Ip6TranslatorId": "ip6-90pt7p9q",
                "Ip6TranslatorName": "kkkk",
                "Vip6": "2402:4e00:20:100::2:1011",
                "IspName": "",
                "TranslatorStatus": "RUNNING",
                "CreatedTime": "2019-01-10T01:33:32Z",
                "Ip6RuleCount": 5
            },
            {
                "Ip6TranslatorId": "ip6-8svxwtts",
                "Ip6TranslatorName": "未命名",
                "Vip6": null,
                "IspName": "",
                "TranslatorStatus": "CREATING",
                "CreatedTime": "2019-01-09T13:50:06Z",
                "Ip6RuleCount": 0
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
                "Ip6RuleCount": 0
            }
        ],
        "RequestId": "cbf8a954-d135-4b52-9935-89e9ec88b536"
    }
}
```

