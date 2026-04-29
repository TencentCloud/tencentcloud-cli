**Example 1: 给特殊的资源授权给某个账号**



Input: 

```
tccli ioa GrantResourcesByAccounts --cli-unfold-argument  \
    --Operations.0.OperationType 1 \
    --Operations.0.ResourceId 7 \
    --Operations.0.ResourceType 1 \
    --Operations.0.ExpireTime 1 \
    --Operations.0.AccountUserId lshawn \
    --Operations.0.MenuId 0
```

Output: 
```
{
    "Response": {
        "RequestId": "72c8b455-b4ac-4604-bd73-844a9c70ba2e"
    }
}
```

