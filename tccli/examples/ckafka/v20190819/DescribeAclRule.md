**Example 1: 枚举ACL**



Input: 

```
tccli ckafka DescribeAclRule --cli-unfold-argument  \
    --InstanceId xxx \
    --RuleName xxx \
    --PatternType xxx \
    --IsSimplified false
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 1,
            "AclRuleList": [
                {
                    "RuleName": "test",
                    "InstanceId": "ckafka-abc",
                    "PatternType": "PRESET",
                    "Pattern": "",
                    "ResourceType": "Topic",
                    "AclList": "[{\"host\":\"*\",\"operation\":\"Read\",\"permissionType\":\"Allow\",\"principal\":\"User:*\"}]",
                    "CreateTimeStamp": "Thu Jun 06 13:07:13 CST 2024",
                    "IsApplied": 0,
                    "UpdateTimeStamp": "Thu Jun 06 13:07:13 CST 2024",
                    "Comment": "",
                    "TopicName": "",
                    "TopicCount": 0,
                    "PatternTypeTitle": "预设策略"
                }
            ]
        },
        "RequestId": "62d589e0-53d5-47e0-95ff-237c48b8fb77"
    }
}
```

