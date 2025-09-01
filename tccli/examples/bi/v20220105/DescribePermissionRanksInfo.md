**Example 1: 根据角色或标签查询行列权限配置**

根据角色或标签查询行列权限配置

Input: 

```
tccli bi DescribePermissionRanksInfo --cli-unfold-argument  \
    --TableId 0 \
    --Mode abc \
    --RoleType abc \
    --RoleId 0 \
    --Type abc \
    --ProjectId 0
```

Output: 
```
{
    "Response": {
        "Msg": "abc",
        "Extra": "abc",
        "Data": {
            "TableId": 0,
            "Type": "abc",
            "Mode": "abc",
            "RulerInfo": "abc",
            "RoleId": 0,
            "RoleType": "abc",
            "RowColumnConfigList": [
                {
                    "RulerInfo": "abc",
                    "TagValueList": [
                        {
                            "Id": 0,
                            "Name": "abc",
                            "Values": [
                                "abc"
                            ]
                        }
                    ]
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

