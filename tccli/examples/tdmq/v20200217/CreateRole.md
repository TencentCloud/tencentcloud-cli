**Example 1: 创建角色**



Input: 

```
tccli tdmq CreateRole --cli-unfold-argument  \
    --RoleName test_role_123 \
    --Remark 创建角色
```

Output: 
```
{
    "Response": {
        "RoleName": "test_role_123",
        "Token": "eyJrZXlJZCI6InN1bmdvxxxxx0X3JvbGVfMyJ9.dbHR8m6gc4L4vZUrodhW_O9bDulZQ6lraNswNLtcUcY",
        "Remark": "创建角色",
        "RequestId": "gggxxxx"
    }
}
```

