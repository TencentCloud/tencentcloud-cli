**Example 1: 查询集团成员列表**



Input: 

```
tccli fwm DescribeOrganMembers --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Members": [
            {
                "AccountGroup": null,
                "AppId": "1300846651",
                "CfwInstanceId": "",
                "CfwManaged": 0,
                "CfwShareRole": "none",
                "CfwShareRoleDisplay": "none",
                "CfwSharerAppId": "",
                "MemberCreateTime": "2022-10-20 15:38:57",
                "MemberId": "mem-1300846651-100011949846",
                "Nickname": "焦糖小蛋糕",
                "NodeName": "Root",
                "PolicyAnalysisEnabled": 0,
                "Role": "admin",
                "RoleDisplay": "admin",
                "SubAccountCount": 0
            },
            {
                "AccountGroup": {
                    "GroupId": "acg-rwqqudnm",
                    "GroupName": "生产账号组1组"
                },
                "AppId": "1300448058",
                "CfwInstanceId": "",
                "CfwManaged": 0,
                "CfwShareRole": "none",
                "CfwShareRoleDisplay": "none",
                "CfwSharerAppId": "",
                "MemberCreateTime": "2025-12-22 20:46:59",
                "MemberId": "mem-1300846651-100011616646",
                "Nickname": "天空之蓝",
                "NodeName": "Root",
                "PolicyAnalysisEnabled": 0,
                "Role": "delegatedAdmin",
                "RoleDisplay": "delegatedAdmin",
                "SubAccountCount": 0
            },
            {
                "AccountGroup": null,
                "AppId": "1327492904",
                "CfwInstanceId": "",
                "CfwManaged": 0,
                "CfwShareRole": "none",
                "CfwShareRoleDisplay": "none",
                "CfwSharerAppId": "",
                "MemberCreateTime": "2024-06-24 14:51:35",
                "MemberId": "mem-1300846651-100037509558",
                "Nickname": "fengqqian",
                "NodeName": "Root",
                "PolicyAnalysisEnabled": 0,
                "Role": "delegatedAdmin",
                "RoleDisplay": "delegatedAdmin",
                "SubAccountCount": 0
            },
            {
                "AccountGroup": null,
                "AppId": "1314933167",
                "CfwInstanceId": "",
                "CfwManaged": 0,
                "CfwShareRole": "none",
                "CfwShareRoleDisplay": "none",
                "CfwSharerAppId": "",
                "MemberCreateTime": "2022-11-09 15:09:35",
                "MemberId": "mem-1300846651-100028354982",
                "Nickname": "少年时",
                "NodeName": "Root",
                "PolicyAnalysisEnabled": 0,
                "Role": "delegatedAdmin",
                "RoleDisplay": "delegatedAdmin",
                "SubAccountCount": 0
            },
            {
                "AccountGroup": null,
                "AppId": "1315399711",
                "CfwInstanceId": "",
                "CfwManaged": 0,
                "CfwShareRole": "none",
                "CfwShareRoleDisplay": "none",
                "CfwSharerAppId": "",
                "MemberCreateTime": "2022-11-26 19:29:43",
                "MemberId": "mem-1300846651-100028671395",
                "Nickname": "美式",
                "NodeName": "Root",
                "PolicyAnalysisEnabled": 0,
                "Role": "member",
                "RoleDisplay": "member",
                "SubAccountCount": 0
            },
            {
                "AccountGroup": null,
                "AppId": "1314503630",
                "CfwInstanceId": "",
                "CfwManaged": 0,
                "CfwShareRole": "none",
                "CfwShareRoleDisplay": "none",
                "CfwSharerAppId": "",
                "MemberCreateTime": "2022-10-20 17:04:50",
                "MemberId": "mem-1300846651-100027980407",
                "Nickname": "测试部门",
                "NodeName": "测试的部门1号",
                "PolicyAnalysisEnabled": 0,
                "Role": "member",
                "RoleDisplay": "member",
                "SubAccountCount": 0
            }
        ],
        "RequestId": "c4feaf81-782f-43cb-9053-4a5982e84a15",
        "TotalCount": 6
    }
}
```

