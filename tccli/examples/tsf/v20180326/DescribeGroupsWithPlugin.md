**Example 1: 查询插件未绑定的分组列表**



Input: 

```
tccli tsf DescribeGroupsWithPlugin --cli-unfold-argument  \
    --PluginId pgn-33pk2soi \
    --GatewayInstanceId gw-ins-33pk2soi \
    --Bound false \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Result": {
            "Content": [
                {
                    "Status": "xx",
                    "UpdatedTime": "xx",
                    "AuthType": "xx",
                    "Description": "xx",
                    "BindedGatewayDeployGroups": [
                        {
                            "DeployGroupId": "xx",
                            "ApplicationName": "xx",
                            "GroupStatus": "xx",
                            "ClusterType": "xx",
                            "DeployGroupName": "xx",
                            "ApplicationType": "xx",
                            "ApplicationId": "xx"
                        }
                    ],
                    "GroupType": "xx",
                    "AclMode": "xx",
                    "ApiCount": 1,
                    "GroupName": "xx",
                    "GroupContext": "xx",
                    "CreatedTime": "xx",
                    "GroupId": "xx"
                },
                {
                    "Status": "xx",
                    "UpdatedTime": "xx",
                    "AuthType": "xx",
                    "Description": "xx",
                    "BindedGatewayDeployGroups": [
                        {
                            "DeployGroupId": "xx",
                            "ApplicationName": "xx",
                            "ApplicationId": "xx",
                            "ClusterType": "xx",
                            "DeployGroupName": "xx",
                            "ApplicationType": "xx",
                            "GroupStatus": "xx"
                        }
                    ],
                    "GroupType": "xx",
                    "AclMode": "xx",
                    "GroupId": "xx",
                    "GroupName": "xx",
                    "GroupContext": "xx",
                    "CreatedTime": "xx",
                    "ApiCount": 3
                }
            ],
            "TotalCount": 2
        },
        "RequestId": "xx"
    }
}
```

