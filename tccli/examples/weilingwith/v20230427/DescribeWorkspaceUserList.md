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
            "Total": 19,
            "Users": [
                {
                    "CreateAt": 1692081934,
                    "DepartmentId": "6",
                    "DepartmentName": "产品部",
                    "Email": "v_leecyli@tencent.com",
                    "LinkFilter": 1,
                    "Phone": "15988886666",
                    "RealName": "v_leecyli",
                    "Status": 1,
                    "TenantId": "100055",
                    "UserId": "0d0a98561b3c4f72963eba5c5fcf56e1",
                    "UserType": "99"
                },
                {
                    "CreateAt": 1691405568,
                    "DepartmentId": "6",
                    "DepartmentName": "产品部",
                    "Email": "vincent_lipc@163.com",
                    "LinkFilter": 1,
                    "Phone": "15656552256",
                    "RealName": "能碳外部演示",
                    "Status": 1,
                    "TenantId": "100055",
                    "UserId": "141ca50134924143b1435919625c7662",
                    "UserType": "3"
                },
                {
                    "CreateAt": 1691390512,
                    "DepartmentId": "32",
                    "DepartmentName": "外部测试",
                    "Email": "caiyitong2009@163.com",
                    "LinkFilter": 1,
                    "Phone": "18611738364",
                    "RealName": "运营外部体验账号",
                    "Status": 1,
                    "TenantId": "100055",
                    "UserId": "0f926d1a7d514629b100b3426bd3c34b",
                    "UserType": "3"
                },
                {
                    "CreateAt": 1691139338,
                    "DepartmentId": "1",
                    "DepartmentName": "研发部",
                    "Email": "richardhhu@tencent.com",
                    "LinkFilter": 1,
                    "Phone": "13988889999",
                    "RealName": "胡辉",
                    "Status": 1,
                    "TenantId": "100055",
                    "UserId": "baea0677027445f49ebcf0ed29480cc2",
                    "UserType": "3"
                },
                {
                    "CreateAt": 1690784410,
                    "DepartmentId": "",
                    "DepartmentName": "",
                    "Email": "213132131@11.com",
                    "LinkFilter": 1,
                    "Phone": "15612345678",
                    "RealName": "liushuang",
                    "Status": 1,
                    "TenantId": "100055",
                    "UserId": "d5f4b7fda1fe472887555704bc6cba0a",
                    "UserType": "99"
                },
                {
                    "CreateAt": 1690777551,
                    "DepartmentId": "",
                    "DepartmentName": "",
                    "Email": "v_ashshliu@tencent.com",
                    "LinkFilter": 1,
                    "Phone": "15801198920",
                    "RealName": "刘爽",
                    "Status": 1,
                    "TenantId": "100055",
                    "UserId": "a0354564529043309b1b7b72e80eb213",
                    "UserType": "99"
                },
                {
                    "CreateAt": 1689755305,
                    "DepartmentId": "6",
                    "DepartmentName": "产品部",
                    "Email": "sineyayan@tencent.com",
                    "LinkFilter": 1,
                    "Phone": "13126071245",
                    "RealName": "sineyayan",
                    "Status": 1,
                    "TenantId": "100055",
                    "UserId": "a76d972c93b44694bd22025f2d3cd359",
                    "UserType": "3"
                },
                {
                    "CreateAt": 1689753730,
                    "DepartmentId": "6",
                    "DepartmentName": "产品部",
                    "Email": "707899536@qq.com",
                    "LinkFilter": 1,
                    "Phone": "19121716602",
                    "RealName": "李鹏程",
                    "Status": 1,
                    "TenantId": "100055",
                    "UserId": "8a9972532d4445cbb81edc27fe49d147",
                    "UserType": "3"
                },
                {
                    "CreateAt": 1686291696,
                    "DepartmentId": "6",
                    "DepartmentName": "产品部",
                    "Email": "604035308@qq.com",
                    "LinkFilter": 1,
                    "Phone": "13713767123",
                    "RealName": "To_Touche",
                    "Status": 1,
                    "TenantId": "100055",
                    "UserId": "c479269ae675480da3b7f5369ebd8618",
                    "UserType": "99"
                },
                {
                    "CreateAt": 1686233544,
                    "DepartmentId": "21",
                    "DepartmentName": "交付组",
                    "Email": "v_yuymiao@tencent.com",
                    "LinkFilter": 1,
                    "Phone": "13299990000",
                    "RealName": "苗元元",
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

