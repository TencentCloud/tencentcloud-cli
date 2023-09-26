**Example 1: 项目-修改用户信息**



Input: 

```
tccli bi ModifyUserRoleProject --cli-unfold-argument  \
    --RoleIdList 100089 \
    --UserId joshshzho \
    --ProjectId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "7be56f43-265c-4ac0-aaa8-3dfbc07aa42f",
        "Extra": "",
        "Data": null,
        "Msg": "success"
    }
}
```

**Example 2: 项目内-修改用户角色权限**



Input: 

```
tccli bi ModifyUserRoleProject --cli-unfold-argument  \
    --RoleIdList 100090 \
    --UserId joshshzho \
    --Email abc@qq.com \
    --ProjectId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "ef53d29a-a89b-4c82-acab-74216bc86bcf",
        "Extra": "",
        "Data": null,
        "Msg": "success"
    }
}
```

