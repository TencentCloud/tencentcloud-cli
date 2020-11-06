**Example 1: 获取资源的规则数**



Input: 

```
tccli dayu DescribeRuleSets --cli-unfold-argument  \
    --Business bgpip \
    --IdList bgpip-000000xe
```

Output: 
```
{
    "RequestId": "677f6c12-f53e-47d4-a4e6-66b932ef950d",
    "L4RuleSets": [
        {
            "Record": [
                {
                    "Key": "Id",
                    "Value": "net-0000000a"
                },
                {
                    "Key": "RuleIdList",
                    "Value": "rule-00000003,rule-00000004,rule-00000005"
                },
                {
                    "Key": "RuleNameList",
                    "Value": "baidu.com,baidu1.com,baidu.com"
                },
                {
                    "Key": "RuleNum",
                    "Value": "3"
                }
            ]
        }
    ],
    "L7RuleSets": [
        {
            "Record": [
                {
                    "Key": "Id",
                    "Value": "net-0000000a"
                },
                {
                    "Key": "RuleIdList",
                    "Value": "rule-00000013,rule-00000014,rule-00000015"
                },
                {
                    "Key": "RuleNameList",
                    "Value": "baidu.com,baidu1.com,baidu.com"
                },
                {
                    "Key": "RuleNum",
                    "Value": "3"
                }
            ]
        }
    ]
}
```

