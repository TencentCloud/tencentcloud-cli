**Example 1: 授权空间列表**

获取用户的空间列表

Input: 

```
tccli oceanus DescribeWorkSpaces --cli-unfold-argument  \
    --Offset 0 \
    --Limit 5 \
    --Filters.0.Name ItemSpaceName \
    --Filters.0.Values def \
    --OrderType 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 25,
        "WorkSpaceSetItem": [
            {
                "SerialId": "spc-1874",
                "WorkSpaceId": "spc-1874",
                "AppId": 1257058945,
                "OwnerUin": "100006386216",
                "CreatorUin": "100006386216",
                "WorkSpaceName": "default0",
                "Region": "ap-guangzhou",
                "CreateTime": "2021-12-10 02:39:54",
                "UpdateTime": "2021-12-10 02:39:54",
                "Status": 2,
                "Description": "子账号在默认空间具有开发者权限，可以在成员管理模块进行限制",
                "ClusterGroupSetItem": [
                    {
                        "ClusterId": "cluster-jphs0vtz",
                        "Name": "k1",
                        "Region": "ap-guangzhou",
                        "Zone": "ap-guangzhou-3",
                        "AppId": 1257058945,
                        "OwnerUin": "100006386216",
                        "CreatorUin": "100006386216",
                        "CuNum": 24,
                        "CuMem": 4,
                        "Status": -1,
                        "StatusDesc": "unknown",
                        "CreateTime": "2020-11-05 09:40:45",
                        "UpdateTime": "2020-11-25 02:47:02",
                        "Remark": "k1",
                        "NetEnvironmentType": 1,
                        "FreeCuNum": 24,
                        "FreeCu": 23.5,
                        "RunningCu": 0,
                        "PayMode": 0
                    }
                ],
                "RoleAuth": [
                    {
                        "Id": 1363,
                        "AppId": 1257058945,
                        "WorkSpaceId": 1874,
                        "WorkSpaceSerialId": "workspace-xxx",
                        "OwnerUin": "100006386216",
                        "CreatorUin": "100006386216",
                        "AuthSubAccountUin": "100006386216",
                        "Permission": 0,
                        "CreateTime": "2021-12-10 02:40:46",
                        "UpdateTime": "2021-12-10 02:40:46",
                        "Status": 2,
                        "RoleName": "name"
                    }
                ],
                "RoleAuthCount": 2,
                "JobsCount": 5
            }
        ],
        "RequestId": "415320BF-0F15-40AB-BB57-8D3B358E0423"
    }
}
```

