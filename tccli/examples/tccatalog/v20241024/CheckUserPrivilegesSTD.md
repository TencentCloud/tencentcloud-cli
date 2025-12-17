**Example 1: 检查用户权限**



Input: 

```
tccli tccatalog CheckUserPrivilegesSTD --cli-unfold-argument  \
    --ResourceType Catalog \
    --Resources.0.Catalog tableeeee111 \
    --Privileges SELECT_TABLE \
    --User 700001601851
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "BatchResults": [
                    false
                ]
            }
        ],
        "RequestId": "30094c5c-251a-4d75-a80d-8490c7290c10"
    }
}
```

