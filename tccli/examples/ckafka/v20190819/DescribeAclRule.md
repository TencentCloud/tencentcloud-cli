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
                    "RuleName": "testRule",
                    "ResourceType": 2
                }
            ]
        },
        "RequestId": "62d589e0-53d5-47e0-95ff-237c48b8fb77"
    }
}
```

