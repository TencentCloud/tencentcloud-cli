**Example 1: 根据规则ID查询规则详情（用户策略）**



Input: 

```
tccli tcss DescribeAbnormalProcessRuleDetail --cli-unfold-argument  \
    --RuleId xxx \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "fee1bdb0-c13f-4c65-b567-8e270df211c1",
        "RuleDetail": {
            "RuleId": "6045892534b9a9000c4ae5ba",
            "IsEnable": true,
            "RuleName": "9999",
            "ChildRules": [
                {
                    "RuleId": "6020e81134b9a9000c50b56a",
                    "RuleMode": "RULE_MODE_ALERT",
                    "ProcessPath": "/bin/ptest",
                    "RuleLevel": "MIDDLE"
                },
                {
                    "RuleId": "60212ddd98dab16785dfeab2",
                    "RuleMode": "RULE_MODE_ALERT",
                    "ProcessPath": "/usr/bin/ps",
                    "RuleLevel": "MIDDLE"
                },
                {
                    "RuleId": "6021472934b9a9000c358fa3",
                    "RuleMode": "RULE_MODE_RELEASE",
                    "ProcessPath": "/usr/bin/top",
                    "RuleLevel": "MIDDLE"
                },
                {
                    "RuleId": "602f603d34b9a9000cb2b405",
                    "RuleMode": "RULE_MODE_ALERT",
                    "ProcessPath": "/usr/bin/tail",
                    "RuleLevel": "MIDDLE"
                },
                {
                    "RuleId": "60326e4434b9a9000c0897a8",
                    "RuleMode": "RULE_MODE_ALERT",
                    "ProcessPath": "/usr/bin/busybox",
                    "RuleLevel": "MIDDLE"
                },
                {
                    "RuleId": "60337df034b9a9000c2240c8",
                    "RuleMode": "RULE_MODE_ALERT",
                    "ProcessPath": "/usr/bin/sss",
                    "RuleLevel": "MIDDLE"
                }
            ],
            "SystemChildRules": [],
            "ImageIds": [
                "sha256:300e315adb2f96afe5f0b2780b87f28ae95231fe3bdd1e16b9ba606307728f55"
            ]
        }
    }
}
```

**Example 2: 根据规则ID查询规则详情（系统策略）**



Input: 

```
tccli tcss DescribeAbnormalProcessRuleDetail --cli-unfold-argument  \
    --RuleId xxx \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "fee1bdb0-c13f-4c65-b567-8e270df211c1",
        "RuleDetail": {
            "RuleId": "6048403bd620f3f9012c521d",
            "IsEnable": true,
            "IsDefault": true,
            "RuleName": "系统策略",
            "ChildRules": [],
            "SystemChildRules": [
                {
                    "RuleId": "100000000000000000000001",
                    "IsEnable": true,
                    "RuleMode": "RULE_MODE_ALERT",
                    "RuleType": "PROXY_TOOL",
                    "RuleLevel": "MIDDLE"
                },
                {
                    "RuleId": "100000000000000000000002",
                    "IsEnable": true,
                    "RuleMode": "RULE_MODE_ALERT",
                    "RuleType": "TRANSFER_CONTROL",
                    "RuleLevel": "MIDDLE"
                },
                {
                    "RuleId": "100000000000000000000003",
                    "IsEnable": true,
                    "RuleMode": "RULE_MODE_ALERT",
                    "RuleType": "ATTACK_CMD",
                    "RuleLevel": "MIDDLE"
                },
                {
                    "RuleId": "100000000000000000000004",
                    "IsEnable": true,
                    "RuleMode": "RULE_MODE_ALERT",
                    "RuleType": "REVERSE_SHELL",
                    "RuleLevel": "MIDDLE"
                },
                {
                    "RuleId": "100000000000000000000005",
                    "IsEnable": true,
                    "RuleMode": "RULE_MODE_ALERT",
                    "RuleType": "FILELESS",
                    "RuleLevel": "MIDDLE"
                },
                {
                    "RuleId": "100000000000000000000006",
                    "IsEnable": true,
                    "RuleMode": "RULE_MODE_ALERT",
                    "RuleType": "RISK_CMD",
                    "RuleLevel": "MIDDLE"
                },
                {
                    "RuleId": "100000000000000000000007",
                    "IsEnable": true,
                    "RuleMode": "RULE_MODE_ALERT",
                    "RuleType": "ABNORMAL_CHILD_PROC",
                    "RuleLevel": "MIDDLE"
                }
            ],
            "ImageIds": [
                "sha256:300e315adb2f96afe5f0b2780b87f28ae95231fe3bdd1e16b9ba606307728f55"
            ]
        }
    }
}
```

**Example 3: 根据事件的镜像ID，查询当前镜像的规则详情（用户策略）**



Input: 

```
tccli tcss DescribeAbnormalProcessRuleDetail --cli-unfold-argument  \
    --ImageId xxx \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "fee1bdb0-c13f-4c65-b567-8e270df211c1",
        "RuleDetail": {
            "RuleId": "6045892534b9a9000c4ae5ba",
            "IsEnable": true,
            "RuleName": "9999",
            "ChildRules": [
                {
                    "RuleId": "6020e81134b9a9000c50b56a",
                    "RuleMode": "RULE_MODE_ALERT",
                    "ProcessPath": "/bin/ptest",
                    "RuleLevel": "MIDDLE"
                },
                {
                    "RuleId": "60212ddd98dab16785dfeab2",
                    "RuleMode": "RULE_MODE_ALERT",
                    "ProcessPath": "/usr/bin/ps",
                    "RuleLevel": "MIDDLE"
                },
                {
                    "RuleId": "6021472934b9a9000c358fa3",
                    "RuleMode": "RULE_MODE_RELEASE",
                    "ProcessPath": "/usr/bin/top",
                    "RuleLevel": "MIDDLE"
                },
                {
                    "RuleId": "602f603d34b9a9000cb2b405",
                    "RuleMode": "RULE_MODE_ALERT",
                    "ProcessPath": "/usr/bin/tail",
                    "RuleLevel": "MIDDLE"
                },
                {
                    "RuleId": "60326e4434b9a9000c0897a8",
                    "RuleMode": "RULE_MODE_ALERT",
                    "ProcessPath": "/usr/bin/busybox",
                    "RuleLevel": "MIDDLE"
                },
                {
                    "RuleId": "60337df034b9a9000c2240c8",
                    "RuleMode": "RULE_MODE_ALERT",
                    "ProcessPath": "/usr/bin/sss",
                    "RuleLevel": "MIDDLE"
                }
            ],
            "SystemChildRules": [],
            "ImageIds": [
                "sha256:300e315adb2f96afe5f0b2780b87f28ae95231fe3bdd1e16b9ba606307728f55"
            ]
        }
    }
}
```

**Example 4: 根据事件的镜像ID，查询当前镜像的规则详情（系统策略）**



Input: 

```
tccli tcss DescribeAbnormalProcessRuleDetail --cli-unfold-argument  \
    --ImageId xxx \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "fee1bdb0-c13f-4c65-b567-8e270df211c1",
        "RuleDetail": {
            "RuleId": "6048403bd620f3f9012c521d",
            "IsEnable": true,
            "IsDefault": true,
            "RuleName": "系统策略",
            "ChildRules": [],
            "SystemChildRules": [
                {
                    "RuleId": "100000000000000000000001",
                    "IsEnable": true,
                    "RuleMode": "RULE_MODE_ALERT",
                    "RuleType": "PROXY_TOOL",
                    "RuleLevel": "MIDDLE"
                },
                {
                    "RuleId": "100000000000000000000002",
                    "IsEnable": true,
                    "RuleMode": "RULE_MODE_ALERT",
                    "RuleType": "TRANSFER_CONTROL",
                    "RuleLevel": "MIDDLE"
                },
                {
                    "RuleId": "100000000000000000000003",
                    "IsEnable": true,
                    "RuleMode": "RULE_MODE_ALERT",
                    "RuleType": "ATTACK_CMD",
                    "RuleLevel": "MIDDLE"
                },
                {
                    "RuleId": "100000000000000000000004",
                    "IsEnable": true,
                    "RuleMode": "RULE_MODE_ALERT",
                    "RuleType": "REVERSE_SHELL",
                    "RuleLevel": "MIDDLE"
                },
                {
                    "RuleId": "100000000000000000000005",
                    "IsEnable": true,
                    "RuleMode": "RULE_MODE_ALERT",
                    "RuleType": "FILELESS",
                    "RuleLevel": "MIDDLE"
                },
                {
                    "RuleId": "100000000000000000000006",
                    "IsEnable": true,
                    "RuleMode": "RULE_MODE_ALERT",
                    "RuleType": "RISK_CMD",
                    "RuleLevel": "MIDDLE"
                },
                {
                    "RuleId": "100000000000000000000007",
                    "IsEnable": true,
                    "RuleMode": "RULE_MODE_ALERT",
                    "RuleType": "ABNORMAL_CHILD_PROC",
                    "RuleLevel": "MIDDLE"
                }
            ],
            "ImageIds": [
                "sha256:300e315adb2f96afe5f0b2780b87f28ae95231fe3bdd1e16b9ba606307728f55"
            ]
        }
    }
}
```

