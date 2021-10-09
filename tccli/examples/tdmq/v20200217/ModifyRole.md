**Example 1: 更新角色**



Input: 

```
tccli tdmq ModifyRole --cli-unfold-argument  \
    --RoleName test_role \
    --Remark 更新角色
```

Output: 
```
{
    "Response": {
        "RoleName": "test_role",
        "Remark": "Remark1",
        "RequestId": "gggxxxx"
    }
}
```

