**Example 1: 根据角色或标签查询行列权限配置**

根据角色或标签查询行列权限配置

Input: 

```
tccli bi DescribePermissionRanksInfo --cli-unfold-argument  \
    --TableId 0 \
    --Mode testdata \
    --RoleType testdata \
    --RoleId 0 \
    --Type testdata \
    --ProjectId 0
```

Output: 
```
{
    "Response": {
        "Msg": "testdata",
        "Extra": "testdata",
        "Data": {
            "TableId": 0,
            "Type": "testdata",
            "Mode": "testdata",
            "RulerInfo": "testdata",
            "RoleId": 0,
            "RoleType": "testdata",
            "RowColumnConfigList": [
                {
                    "RulerInfo": "testdata",
                    "TagValueList": [
                        {
                            "Id": 0,
                            "Name": "testdata",
                            "Values": [
                                "testdata"
                            ]
                        }
                    ]
                }
            ]
        },
        "RequestId": "testdata"
    }
}
```

