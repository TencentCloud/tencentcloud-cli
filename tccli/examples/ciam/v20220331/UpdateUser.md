**Example 1: 更新用户**



Input: 

```
tccli ciam UpdateUser --cli-unfold-argument  \
    --UserName xx \
    --UserStoreId xx \
    --UserGroup xxx \
    --UserId xx \
    --Birthdate 0 \
    --PhoneNumber xx \
    --Address xx \
    --Nickname xx \
    --Email xx \
    --CustomizationAttributes.0.Name xx \
    --CustomizationAttributes.0.Value xx \
    --CustomizationAttributes.0.Type xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xxx",
        "User": null
    }
}
```

