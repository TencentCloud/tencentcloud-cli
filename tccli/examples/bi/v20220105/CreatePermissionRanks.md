**Example 1: 创建行列权限**

创建行列权限

Input: 

```
tccli bi CreatePermissionRanks --cli-unfold-argument  \
    --TableId 0 \
    --Mode abc \
    --RoleType abc \
    --RoleId 0 \
    --RulerInfo abc \
    --Type abc \
    --OpenStatus abc \
    --ProjectId 0 \
    --RowColumnConfigList.0.RulerInfo abc \
    --RowColumnConfigList.0.TagValueList.0.Id 0 \
    --RowColumnConfigList.0.TagValueList.0.Name abc \
    --RowColumnConfigList.0.TagValueList.0.Values abc
```

Output: 
```
{
    "Response": {
        "Msg": "abc",
        "Extra": "abc",
        "Data": "abc",
        "RequestId": "abc"
    }
}
```

