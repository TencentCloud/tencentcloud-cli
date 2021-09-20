**Example 1: 示例**



Input: 

```
tccli eiam DescribeOrgResourcesAuthorization --cli-unfold-argument  \
    --OrgNodeId xx \
    --ApplicationId xx
```

Output: 
```
{
    "Response": {
        "RequestId": "10df84ec-33d8-4fe1-a180-960aaa5c746a",
        "ApplicationId": "f6f29e24-ffc2-456c-b815-532291bc96af",
        "OrgNodeId": "46165edc-4fc0-46d7-8973-453fb58fe24f",
        "OrgNodeName": "csg",
        "TotalCount": 1,
        "OrgNodePath": "tencent/csg",
        "AuthorizationOrgResourceList": [
            {
                "ResourceId": "fe211d3a-6a08-435a-a4b4-5537176acd2e",
                "ResourceType": "resource",
                "Resource": "service-ovwon6kp：service-ovwonooo"
            }
        ]
    }
}
```

