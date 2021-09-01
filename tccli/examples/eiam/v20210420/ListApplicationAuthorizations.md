**Example 1: 请求示例**



Input: 

```
tccli eiam ListApplicationAuthorizations --cli-unfold-argument  \
    --EntityType OrgNode
```

Output: 
```
{
    "Response": {
        "AuthorizationInfoList": [
            {
                "EntityId": "xxx",
                "LastModifiedDate": "2021-03-25T19:48:29.504+0800",
                "EntityName": "腾讯企业邮箱1",
                "AppId": "xxx",
                "AppName": "CAS（标准）1",
                "AuthorizationId": "xxx"
            },
            {
                "EntityId": "xxx",
                "LastModifiedDate": "2021-03-30T18:05:33.143+0800",
                "EntityName": "11",
                "AppId": "xxx",
                "AppName": "腾讯企业邮箱2",
                "AuthorizationId": "xxx"
            }
        ],
        "TotalCount": 4,
        "RequestId": "123"
    }
}
```

