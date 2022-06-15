**Example 1: 创建用户**



Input: 

```
tccli ciam CreateUser --cli-unfold-argument  \
    --UserName xx \
    --UserStoreId xx \
    --UserGroup xxx \
    --Birthdate 0 \
    --PhoneNumber xx \
    --Address xx \
    --Password xx \
    --Nickname xx \
    --Email xx \
    --CustomizationAttributes.0.Name xx \
    --CustomizationAttributes.0.Value xx
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

