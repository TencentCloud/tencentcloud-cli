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
            "TotalCount": 0,
            "Content": [
                {
                    "GroupId": "abc",
                    "GroupName": "abc",
                    "GroupContext": "abc",
                    "AuthType": "abc",
                    "Status": "abc",
                    "CreatedTime": "abc",
                    "UpdatedTime": "abc",
                    "BindedGatewayDeployGroups": [
                        {
                            "DeployGroupId": "abc",
                            "DeployGroupName": "abc",
                            "ApplicationId": "abc",
                            "ApplicationName": "abc",
                            "ApplicationType": "abc",
                            "GroupStatus": "abc",
                            "ClusterType": "abc"
                        }
                    ],
                    "ApiCount": 0,
                    "AclMode": "abc",
                    "Description": "abc",
                    "GroupType": "abc",
                    "GatewayInstanceType": "abc",
                    "GatewayInstanceId": "abc",
                    "NamespaceNameKey": "abc",
                    "ServiceNameKey": "abc",
                    "NamespaceNameKeyPosition": "abc",
                    "ServiceNameKeyPosition": "abc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

