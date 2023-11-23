**Example 1: 查询租户人员列表**

查询租户人员列表

Input: 

```
tccli weilingwith DescribeTenantUserList --cli-unfold-argument  \
    --Offset 1 \
    --Limit 1 \
    --TenantId 1 \
    --ApplicationToken Z2GWsZyAcnKt1zIK65FQz5XsFk5nTKqx
```

Output: 
```
{
    "Response": {
        "RequestId": "2a9b97e6-3f19-43ea-9ec6-37985e4eac99",
        "Result": {
            "Total": 28,
            "Users": [
                {
                    "BelongTeam": 0,
                    "CreateAt": 1691565476,
                    "DepartmentId": "6",
                    "DepartmentName": "产品部",
                    "DepartmentUserId": 431,
                    "Email": "test@tencent.com",
                    "Password": "",
                    "Phone": "159****6666",
                    "RealName": "test",
                    "Status": 1,
                    "TenantId": "100055",
                    "UpdateAt": 1691745205,
                    "UserGroup": "",
                    "UserId": "0d0a98561b3c4f72963eba5c5fcf56e1",
                    "UserName": "",
                    "UserType": "99"
                }
            ]
        }
    }
}
```

