**Example 1: 修改用户角色信息**



Input: 

```
tccli bi ModifyUserRole --cli-unfold-argument  \
    --RoleIdList 100090 \
    --UserId joshshzho \
    --Email abc@qq.com
```

Output: 
```
{
    "Response": {
        "RequestId": "933660c5-a247-4068-a852-c3eaf0e93684",
        "Extra": "",
        "Data": null,
        "Msg": "success"
    }
}
```

**Example 2: demo**



Input: 

```
tccli bi ModifyUserRole --cli-unfold-argument  \
    --UserName tommyho \
    --AreaCode 086 \
    --UserId tommyho \
    --PhoneNumber 123456 \
    --RoleIdList 100099 \
    --Email 123@qq.com
```

Output: 
```
{
    "Response": {
        "Msg": "success",
        "RequestId": "6b573965-cda5-4c95-a66a-fd1bd6d77c5c",
        "Extra": "",
        "Data": null
    }
}
```

