**Example 1: 查询API 分组信息列表**



Input: 

```
tccli tsf DescribeApiGroups --cli-unfold-argument  \
    --GatewayInstanceId gw-ins-szesmg28
```

Output: 
```
{
    "Response": {
        "RequestId": "db4da85c-a228-4dca-9326-460f19a689e6",
        "Result": {
            "Content": [
                {
                    "AclMode": "none",
                    "ApiCount": 4,
                    "AuthType": "none",
                    "BindedGatewayDeployGroups": [
                        {
                            "ApplicationId": "application-yq58wpey",
                            "ApplicationName": "heihuli-gw",
                            "ApplicationType": "V",
                            "ClusterType": "V",
                            "DeployGroupId": "group-ym9mqx2a",
                            "DeployGroupName": "heihuli-zuul-unit",
                            "GroupStatus": null
                        }
                    ],
                    "CreatedTime": "2023-01-10 17:37:26",
                    "Description": "",
                    "GatewayInstanceId": "gw-ins-szesmg28",
                    "GatewayInstanceIdList": null,
                    "GatewayInstanceType": null,
                    "GroupContext": "/heihuli",
                    "GroupId": "grp-ptrhio2l",
                    "GroupName": "heihuli",
                    "GroupType": "ms",
                    "NamespaceNameKey": null,
                    "NamespaceNameKeyPosition": "path",
                    "ServiceNameKey": null,
                    "ServiceNameKeyPosition": "path",
                    "Status": "released",
                    "UpdatedTime": "2023-01-10 22:09:34"
                }
            ],
            "TotalCount": 1
        }
    }
}
```

