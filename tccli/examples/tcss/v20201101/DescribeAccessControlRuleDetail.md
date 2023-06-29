**Example 1: 根据规则ID查询规则详情（用户策略）**



Input: 

```
tccli tcss DescribeAccessControlRuleDetail --cli-unfold-argument  \
    --RuleId xxx \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "1af946cb-d3d5-4b03-bbfc-3d5ad306f753",
        "RuleDetail": {
            "RuleId": "6045899634b9a9000c4ae5bb",
            "IsEnable": true,
            "IsDefault": false,
            "RuleName": "kkkkk",
            "ChildRules": [
                {
                    "RuleId": "603279ba34b9a9000c0897ae",
                    "RuleMode": "RULE_MODE_HOLDUP",
                    "ProcessPath": "/usr/bin/vi",
                    "TargetFilePath": "*.txt"
                },
                {
                    "RuleId": "60327a7b34b9a9000c0897af",
                    "RuleMode": "RULE_MODE_ALERT",
                    "ProcessPath": "/data/a.out",
                    "TargetFilePath": "/tmp/test2.txt"
                },
                {
                    "RuleId": "6033081234b9a9000c0897b0",
                    "RuleMode": "RULE_MODE_HOLDUP",
                    "ProcessPath": "/usr/bin/coreutils",
                    "TargetFilePath": "/tmp/test.txt"
                },
                {
                    "RuleId": "60337e1034b9a9000c2240c9",
                    "RuleMode": "RULE_MODE_ALERT",
                    "ProcessPath": "/data/a.out",
                    "TargetFilePath": "/tmp/test.txt"
                },
                {
                    "RuleId": "60361e8234b9a9000cf7a3ee",
                    "RuleMode": "RULE_MODE_ALERT",
                    "ProcessPath": "/usr/bin/vi",
                    "TargetFilePath": "*.HTML"
                },
                {
                    "RuleId": "603772d334b9a9000cd92ae8",
                    "RuleMode": "RULE_MODE_ALERT",
                    "ProcessPath": "/usr/bin/iv",
                    "TargetFilePath": "*.HTML"
                },
                {
                    "RuleId": "6045899634b9a9000c4ae5bc",
                    "RuleMode": "RULE_MODE_RELEASE",
                    "ProcessPath": "/usr/bin/vi",
                    "TargetFilePath": "/1.txt"
                }
            ],
            "SystemChildRules": [],
            "ImageIds": [
                "sha256:300e315adb2f96afe5f0b2780b87f28ae95231fe3bdd1e16b9ba606307728f55",
                "sha256:e50c909a8df2b7c8b92a6e8730e210ebe98e5082871e66edd8ef4d90838cbd25",
                "sha256:298ec0e28760b8eb1aad79711dc29c19041c61d7cf342dd1f445e91f30500549"
            ]
        }
    }
}
```

**Example 2: 根据事件的镜像ID，查询当前镜像的规则详情（用户策略）**



Input: 

```
tccli tcss DescribeAccessControlRuleDetail --cli-unfold-argument  \
    --ImageId xxx \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "1af946cb-d3d5-4b03-bbfc-3d5ad306f753",
        "RuleDetail": {
            "RuleId": "6045899634b9a9000c4ae5bb",
            "IsEnable": true,
            "IsDefault": false,
            "RuleName": "kkkkk",
            "ChildRules": [
                {
                    "RuleId": "603279ba34b9a9000c0897ae",
                    "RuleMode": "RULE_MODE_HOLDUP",
                    "ProcessPath": "/usr/bin/vi",
                    "TargetFilePath": "*.txt"
                },
                {
                    "RuleId": "60327a7b34b9a9000c0897af",
                    "RuleMode": "RULE_MODE_ALERT",
                    "ProcessPath": "/data/a.out",
                    "TargetFilePath": "/tmp/test2.txt"
                },
                {
                    "RuleId": "6033081234b9a9000c0897b0",
                    "RuleMode": "RULE_MODE_HOLDUP",
                    "ProcessPath": "/usr/bin/coreutils",
                    "TargetFilePath": "/tmp/test.txt"
                },
                {
                    "RuleId": "60337e1034b9a9000c2240c9",
                    "RuleMode": "RULE_MODE_ALERT",
                    "ProcessPath": "/data/a.out",
                    "TargetFilePath": "/tmp/test.txt"
                },
                {
                    "RuleId": "60361e8234b9a9000cf7a3ee",
                    "RuleMode": "RULE_MODE_ALERT",
                    "ProcessPath": "/usr/bin/vi",
                    "TargetFilePath": "*.HTML"
                },
                {
                    "RuleId": "603772d334b9a9000cd92ae8",
                    "RuleMode": "RULE_MODE_ALERT",
                    "ProcessPath": "/usr/bin/iv",
                    "TargetFilePath": "*.HTML"
                },
                {
                    "RuleId": "6045899634b9a9000c4ae5bc",
                    "RuleMode": "RULE_MODE_RELEASE",
                    "ProcessPath": "/usr/bin/vi",
                    "TargetFilePath": "/1.txt"
                }
            ],
            "SystemChildRules": [],
            "ImageIds": [
                "sha256:300e315adb2f96afe5f0b2780b87f28ae95231fe3bdd1e16b9ba606307728f55",
                "sha256:e50c909a8df2b7c8b92a6e8730e210ebe98e5082871e66edd8ef4d90838cbd25",
                "sha256:298ec0e28760b8eb1aad79711dc29c19041c61d7cf342dd1f445e91f30500549"
            ]
        }
    }
}
```

**Example 3: 根据规则ID查询规则详情（系统策略）**



Input: 

```
tccli tcss DescribeAccessControlRuleDetail --cli-unfold-argument  \
    --RuleId xxx \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "1af946cb-d3d5-4b03-bbfc-3d5ad306f753",
        "RuleDetail": {
            "RuleId": "60484042d620f3f9012c521e",
            "IsEnable": true,
            "IsDefault": true,
            "RuleName": "kkkkk",
            "ChildRules": [],
            "SystemChildRules": [
                {
                    "RuleId": "200000000000000000000001",
                    "IsEnable": true,
                    "RuleMode": "RULE_MODE_ALERT",
                    "RuleType": "CHANGE_CRONTAB"
                },
                {
                    "RuleId": "200000000000000000000002",
                    "IsEnable": true,
                    "RuleMode": "RULE_MODE_ALERT",
                    "RuleType": "CHANGE_SYS_BIN"
                },
                {
                    "RuleId": "200000000000000000000003",
                    "IsEnable": true,
                    "RuleMode": "RULE_MODE_ALERT",
                    "RuleType": "CHANGE_USRCFG"
                }
            ],
            "ImageIds": [
                "sha256:300e315adb2f96afe5f0b2780b87f28ae95231fe3bdd1e16b9ba606307728f55",
                "sha256:e50c909a8df2b7c8b92a6e8730e210ebe98e5082871e66edd8ef4d90838cbd25",
                "sha256:298ec0e28760b8eb1aad79711dc29c19041c61d7cf342dd1f445e91f30500549"
            ]
        }
    }
}
```

**Example 4: 根据事件的镜像ID，查询当前镜像的规则详情（系统策略）**



Input: 

```
tccli tcss DescribeAccessControlRuleDetail --cli-unfold-argument  \
    --RuleId xxx \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "1af946cb-d3d5-4b03-bbfc-3d5ad306f753",
        "RuleDetail": {
            "RuleId": "60484042d620f3f9012c521e",
            "IsEnable": true,
            "IsDefault": true,
            "RuleName": "kkkkk",
            "ChildRules": [],
            "SystemChildRules": [
                {
                    "RuleId": "200000000000000000000001",
                    "IsEnable": true,
                    "RuleMode": "RULE_MODE_ALERT",
                    "RuleType": "CHANGE_CRONTAB"
                },
                {
                    "RuleId": "200000000000000000000002",
                    "IsEnable": true,
                    "RuleMode": "RULE_MODE_ALERT",
                    "RuleType": "CHANGE_SYS_BIN"
                },
                {
                    "RuleId": "200000000000000000000003",
                    "IsEnable": true,
                    "RuleMode": "RULE_MODE_ALERT",
                    "RuleType": "CHANGE_USRCFG"
                }
            ],
            "ImageIds": [
                "sha256:300e315adb2f96afe5f0b2780b87f28ae95231fe3bdd1e16b9ba606307728f55",
                "sha256:e50c909a8df2b7c8b92a6e8730e210ebe98e5082871e66edd8ef4d90838cbd25",
                "sha256:298ec0e28760b8eb1aad79711dc29c19041c61d7cf342dd1f445e91f30500549"
            ]
        }
    }
}
```

