**Example 1: 查询项目空间人员列表**

查询项目空间人员列表

Input: 

```
tccli weilingwith DescribeWorkspaceUserList --cli-unfold-argument  \
    --Offset 1 \
    --Limit 10 \
    --WorkspaceId 1016 \
    --ApplicationToken o9ftuUNOFkOVf2o5etJ0nHou396ufAes
```

Output: 
```
{
    "Response": {
        "RequestId": "68f43238-01a6-46c6-9204-f23cc3983756",
        "Result": {
            "Total": 3,
            "Users": [
                {
                    "CreateAt": 1692081934,
                    "DepartmentId": "6",
                    "DepartmentName": "产品部",
                    "Email": "test1@tencent.com",
                    "LinkFilter": 1,
                    "Phone": "159****6666",
                    "RealName": "test1",
                    "Status": 1,
                    "TenantId": "100055",
                    "UserId": "0d0a98561b3c4f72963eba5c5fcf56e1",
                    "UserType": "99"
                },
                {
                    "CreateAt": 1691139338,
                    "DepartmentId": "1",
                    "DepartmentName": "研发部",
                    "Email": "test2 @tencent.com",
                    "LinkFilter": 1,
                    "Phone": "139****9999",
                    "RealName": "test2",
                    "Status": 1,
                    "TenantId": "100055",
                    "UserId": "baea0677027445f49ebcf0ed29480cc2",
                    "UserType": "3"
                },
                {
                    "CreateAt": 1686233544,
                    "DepartmentId": "21",
                    "DepartmentName": "交付组",
                    "Email": "test3 @tencent.com",
                    "LinkFilter": 1,
                    "Phone": "132****0000",
                    "RealName": "test3",
                    "Status": 1,
                    "TenantId": "100055",
                    "UserId": "159ac75273614918be42b3b0a208d1ab",
                    "UserType": "3"
                }
            ]
        }
    }
}
```

