**Example 1: 获取角色列表**



Input: 

```
tccli cam DescribeRoleList --cli-unfold-argument  \
    --Rp 5 \
    --Page 1
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AddTime": "2020-11-28 10:05:52",
                "ConsoleLogin": 0,
                "DeletionTaskId": null,
                "Description": "当前角色为腾讯云自动化助手 (TAT)服务相关角色，该角色将在已关联策略的权限范围内访问您的其他云服务资源。",
                "PolicyDocument": "{\"version\":\"2.0\",\"statement\":[{\"action\":\"sts:AssumeRole\",\"effect\":\"allow\",\"principal\":{\"service\":[\"command.tat.cloud.tencent.com\"]}}]}",
                "RoleId": "4611686018433460000",
                "RoleName": "TAT_QCSLinkedRoleInCommand",
                "RoleType": "service_linked",
                "SessionDuration": 43200,
                "Tags": [],
                "UpdateTime": "2020-11-28 10:05:52"
            },
            {
                "AddTime": "2020-06-28 12:07:06",
                "ConsoleLogin": 0,
                "DeletionTaskId": null,
                "Description": "当前角色为云服务器（CVM）服务相关角色，该角色将在已关联策略的权限范围内访问您的其他云服务资源。",
                "PolicyDocument": "{\"version\":\"2.0\",\"statement\":[{\"action\":\"sts:AssumeRole\",\"effect\":\"allow\",\"principal\":{\"service\":[\"cvmsmartdiagnostic.cvm.cloud.tencent.com\"]}}]}",
                "RoleId": "4611686018432380000",
                "RoleName": "CVM_QCSLinkedRoleInCVMSmartDiagnostic",
                "RoleType": "service_linked",
                "SessionDuration": 43200,
                "Tags": [
                    {
                        "Key": "K1",
                        "Value": "V7"
                    }
                ],
                "UpdateTime": "2020-06-28 12:07:06"
            }
        ],
        "RequestId": "36d78422-f6ce-4edb-a5a0-a217b366aa70",
        "TotalNum": 2
    }
}
```

