**Example 1: 移除角色权限**



Input: 

```
tccli tccatalog RevokeUserPrivilegesSTD --cli-unfold-argument  \
    --ResourceType Catalog \
    --Resources.0.Catalog tableeeee111 \
    --Privileges SELECT_TABLE \
    --Roles justtest008
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Item": "tableeeee111",
                "Reason": "",
                "Result": true
            }
        ],
        "RequestId": "9268dafc-6eb4-429f-95f0-49b91b55e4e5"
    }
}
```

