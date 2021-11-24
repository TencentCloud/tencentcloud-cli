**Example 1: 枚举ACL**



Input: 

```
tccli ckafka DescribeACL --cli-unfold-argument  \
    --InstanceId xxx \
    --ResourceType 2 \
    --ResourceName xxx
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 1,
            "AclList": [
                {
                    "ResourceType": 2,
                    "ResourceName": "test",
                    "Principal": "User:test",
                    "Host": "*",
                    "Operation": 3,
                    "PermissionType": 3
                }
            ]
        },
        "RequestId": "62d589e0-53d5-47e0-95ff-237c48b8fb77"
    }
}
```

