**Example 1: 示例**



Input: 

```
tccli eiam DescribeUserResourcesAuthorization --cli-unfold-argument  \
    --UserName xx \
    --UserId xx \
    --IncludeInheritedAuthorizations True \
    --ApplicationId xx
```

Output: 
```
{
    "Response": {
        "RequestId": "10df84ec-33d8-4fe1-a180-960aaa5c746a",
        "ApplicationId": "7107ee0d-e556-47db-8fca-e6d1fc910dd2",
        "ApplicationAccounts": [
            "iamadmin"
        ],
        "UserId": "1we234c7f-56b0-4c3a-9ae5-17baeb0u5643",
        "UserName": "zhangsan",
        "AuthorizationUserResourceList": [
            {
                "InheritedForm": {
                    "UserGroupIds": [
                        "8580d166-2a25-45eb-beff-3085f5464deb",
                        "2222d166-2a25-45eb-beff-3085f5234ed"
                    ],
                    "OrgNodeIds": [
                        "823445-2a25-45eb-beff-3085f54645555"
                    ]
                },
                "ApplicationAccounts": [
                    "iamadmin"
                ],
                "ResourceId": "8ae33c7f-56b0-4c3a-9ae5-17baeb0d7940",
                "ResourceType": "resourceGroup",
                "Resource": "service-888:*"
            },
            {
                "InheritedForm": {
                    "UserGroupIds": [
                        "8580d166-2a25-45eb-beff-3085f5464deb"
                    ],
                    "OrgNodeIds": [
                        "823445-2a25-45eb-beff-3085f54645555"
                    ]
                },
                "ApplicationAccounts": [
                    "iamadmin"
                ],
                "ResourceId": "8ae33c7f-56b0-4c3a-9ae5-17baeb0d7940",
                "ResourceType": "resourceGroup",
                "Resource": "service-888:*"
            },
            {
                "InheritedForm": {
                    "UserGroupIds": [],
                    "OrgNodeIds": []
                },
                "ApplicationAccounts": [
                    "iamadmin"
                ],
                "ResourceId": "8ae33c7f-56b0-4c3a-9ae5-17baeb0d7940",
                "ResourceType": "resourceGroup",
                "Resource": "service-888:*"
            }
        ]
    }
}
```

