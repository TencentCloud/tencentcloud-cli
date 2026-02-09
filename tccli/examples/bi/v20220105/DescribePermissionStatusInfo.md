**Example 1: 项目内角色列表接口示例**

项目内角色列表接口示例

Input: 

```
tccli bi DescribePermissionStatusInfo --cli-unfold-argument  \
    --TableId -4052 \
    --Type fugiat magna velit ea dolore \
    --ProjectId 1231
```

Output: 
```
{
    "Response": {
        "Msg": "默认业务成功",
        "RequestId": "dfcd12ec-6920-42a1-a758-7a10fcc4a60a",
        "Extra": "",
        "Data": {
            "TableId": 0,
            "Type": "row",
            "Mode": "specify",
            "OpenStatus": "open",
            "RoleType": "roles",
            "RoleId": 0
        }
    }
}
```

