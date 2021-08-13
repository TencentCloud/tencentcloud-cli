**Example 1: 示例**



Input: 

```
tccli eiam DescribeUserGroupResourcesAuthorization --cli-unfold-argument  \
    --ApplicationId xx \
    --UserGroupId xx
```

Output: 
```
{
    "Response": {
        "RequestId": "10df84ec-33d8-4fe1-a180-960aaa5c746a",
        "ApplicationId": "f6f29e24-ffc2-456c-b815-532291bc96af",
        "UserGroupId": "1we234c7f-56b0-4c3a-9ae5-17baeb0u5643",
        "UserGroupName": "用户组1",
        "AuthorizationUserGroupResourceList": [
            {
                "ResourceId": "8ae33c7f-56b0-4c3a-9ae5-17baeb0d7940",
                "ResourceType": "resource",
                "Resource": "service-ovwon6kp：service-23errrt"
            }
        ]
    }
}
```

