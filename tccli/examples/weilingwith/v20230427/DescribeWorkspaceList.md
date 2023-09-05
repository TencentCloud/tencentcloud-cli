**Example 1: 查询项目空间列表**

查询项目空间列表

Input: 

```
tccli weilingwith DescribeWorkspaceList --cli-unfold-argument  \
    --ApplicationToken XggJvayJyusfUwuoJ2OlT4Z2YAVq6bVo
```

Output: 
```
{
    "Response": {
        "RequestId": "d04a9bab-dd91-4999-8584-bbc4d5203d50",
        "Result": {
            "List": [
                {
                    "ChineseName": "lv测试空间",
                    "Description": "lv测试空间",
                    "EnglishName": "",
                    "IsCommWorkspace": false,
                    "Status": 0,
                    "TenantId": 100055,
                    "ValidityEndTime": "1744387200",
                    "ValidityStartTime": "1682524800",
                    "WorkspaceId": 1092
                },
                {
                    "ChineseName": "RayDataWeb",
                    "Description": "RayDataWeb测试使用测完后删除",
                    "EnglishName": "",
                    "IsCommWorkspace": false,
                    "Status": 0,
                    "TenantId": 100055,
                    "ValidityEndTime": "2000390400",
                    "ValidityStartTime": "1684684800",
                    "WorkspaceId": 1166
                },
                {
                    "ChineseName": "华东项目空间",
                    "Description": "演练项目空间",
                    "EnglishName": "",
                    "IsCommWorkspace": false,
                    "Status": 0,
                    "TenantId": 100055,
                    "ValidityEndTime": "1693411200",
                    "ValidityStartTime": "1682870400",
                    "WorkspaceId": 1175
                },
                {
                    "ChineseName": "ces",
                    "Description": "123",
                    "EnglishName": "",
                    "IsCommWorkspace": false,
                    "Status": 1,
                    "TenantId": 100055,
                    "ValidityEndTime": "1688400000",
                    "ValidityStartTime": "1688313600",
                    "WorkspaceId": 1524
                },
                {
                    "ChineseName": "公共空间",
                    "Description": "租户默认工作空间",
                    "EnglishName": "comm_workspace",
                    "IsCommWorkspace": true,
                    "Status": 0,
                    "TenantId": 100055,
                    "ValidityEndTime": "4834882335",
                    "ValidityStartTime": "1681282335",
                    "WorkspaceId": 1015
                },
                {
                    "ChineseName": "华南园区项目",
                    "Description": "华南园区项目",
                    "EnglishName": "",
                    "IsCommWorkspace": false,
                    "Status": 0,
                    "TenantId": 100055,
                    "ValidityEndTime": "2153664000",
                    "ValidityStartTime": "1680278400",
                    "WorkspaceId": 1016
                },
                {
                    "ChineseName": "华北园区项目",
                    "Description": "华北园区项目",
                    "EnglishName": "",
                    "IsCommWorkspace": false,
                    "Status": 0,
                    "TenantId": 100055,
                    "ValidityEndTime": "2153664000",
                    "ValidityStartTime": "1680278400",
                    "WorkspaceId": 1018
                },
                {
                    "ChineseName": "test",
                    "Description": "ceshi",
                    "EnglishName": "",
                    "IsCommWorkspace": false,
                    "Status": 0,
                    "TenantId": 100055,
                    "ValidityEndTime": "1747584000",
                    "ValidityStartTime": "1685289600",
                    "WorkspaceId": 1263
                },
                {
                    "ChineseName": "report2test",
                    "Description": "report2test",
                    "EnglishName": "",
                    "IsCommWorkspace": false,
                    "Status": 0,
                    "TenantId": 100055,
                    "ValidityEndTime": "2192976000",
                    "ValidityStartTime": "1687795200",
                    "WorkspaceId": 1439
                }
            ]
        }
    }
}
```

