**Example 1: 创建行列权限**

创建行列权限

Input: 

```
tccli bi CreatePermissionRanks --cli-unfold-argument  \
    --TableId 10628115 \
    --Mode all \
    --RoleType others \
    --RoleId 0 \
    --RulerInfo {"Logic":"and","Items":[]} \
    --Type column \
    --OpenStatus open \
    --ProjectId 11055177
```

Output: 
```
{
    "Response": {
        "Msg": "默认业务成功",
        "RequestId": "131ecec6-e8c7-4147-af1c-3c5725307583",
        "Extra": "",
        "Data": null
    }
}
```

