**Example 1: success**



Input: 

```
tccli bi ModifyUserDetailInfo --cli-unfold-argument  \
    --UserName jacklliu \
    --UserId 700001088309 \
    --RoleIdList 100635 \
    --UserGroupIdList 259 267 262 261 268 269 \
    --LoginSecurityStatus 0 \
    --ResetPassWordTip 0 \
    --ForceResetPassWord 0 \
    --PasswordExpired 90
```

Output: 
```
{
    "Response": {
        "Msg": "默认业务成功",
        "RequestId": "32a64ac7-8a34-4be8-9a42-9f8780e71a5e",
        "Extra": "",
        "Data": null
    }
}
```

