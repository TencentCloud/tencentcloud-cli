**Example 1: 枚举ACL**



Input: 

```
tccli ckafka DescribeACL --cli-unfold-argument  \
    --InstanceId ckafka-test \
    --ResourceType 2 \
    --ResourceName resourcename
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
                    "ResourceName": "ResourcetTest",
                    "Principal": "User:test",
                    "Host": "10.1.2.4",
                    "Operation": 3,
                    "PermissionType": 3
                }
            ]
        },
        "RequestId": "62d589e0-53d5-47e0-95ff-237c48b8fb77"
    }
}
```

