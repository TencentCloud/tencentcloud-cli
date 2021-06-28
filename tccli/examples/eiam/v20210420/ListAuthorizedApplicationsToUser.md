**Example 1: 请求示例**



Input: 

```
tccli eiam ListAuthorizedApplicationsToUser --cli-unfold-argument  \
    --IncludeInheritedAuthorizations True \
    --UserId xx
```

Output: 
```
{
    "Response": {
        "RequestId": "6f5159d1-213e-4daf-86b5-0bc19a93c4c0",
        "ApplicationAuthorizationInfo": [
            {
                "InheritedForm": {
                    "UserGroupIds": [
                        "8580d166-2a25-45eb-beff-3085f5464deb",
                        "f72f0340-fa3d-4506-8a24-abb7d4ed8d36"
                    ],
                    "OrgNodeIds": [
                        "c41d73c6-5eb4-44ee-878b-45a40fddf14a"
                    ]
                },
                "ApplicationAccounts": [
                    "iamadmin"
                ],
                "ApplicationId": "7107ee0d-e556-47db-8fca-e6d1fc910dd2"
            },
            {
                "InheritedForm": {
                    "UserGroupIds": [],
                    "OrgNodeIds": [
                        "177b7049-a649-4bef-8d20-ce66cabc9fe7",
                        "28d0f6a3-41b3-499c-afcb-78f707ef71a5"
                    ]
                },
                "ApplicationAccounts": [
                    "iamadmin"
                ],
                "ApplicationId": "3f3386a3-35e3-49b6-bc52-cbe98381b4d4"
            }
        ]
    }
}
```

