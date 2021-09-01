**Example 1: 查询某个网关绑定的API 分组信息列表**



Input: 

```
tccli tsf DescribeGroupGateways --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --GatewayDeployGroupId group-fdsfdsfds
```

Output: 
```
{
    "Response": {
        "Result": {
            "Content": [
                {
                    "Status": "drafted",
                    "UpdatedTime": "2019-06-20 15:51:28",
                    "AuthType": "none",
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
                    "GroupType": "ms",
                    "AclMode": "xx",
                    "ApiCount": 0,
                    "GroupName": "xx",
                    "GroupContext": "/xx",
                    "CreatedTime": "2019-06-20 15:51:28",
                    "GroupId": "grp-e42d597"
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "xx"
    }
}
```

