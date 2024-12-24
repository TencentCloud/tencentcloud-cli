**Example 1: 查询某个网关绑定的API 分组信息列表**



Input: 

```
tccli tsf DescribeGroupGateways --cli-unfold-argument  \
    --GatewayDeployGroupId group-yd3b588a \
    --SearchWord grpName \
    --Offset 0 \
    --Limit 5
```

Output: 
```
{
    "Response": {
        "RequestId": "c52f74e0-ed84-40b2-a57c-6489bd4eb700",
        "Result": {
            "Content": [
                {
                    "AclMode": null,
                    "ApiCount": 0,
                    "AuthType": null,
                    "BindedGatewayDeployGroups": [],
                    "CreatedTime": null,
                    "Description": null,
                    "GatewayInstanceId": null,
                    "GatewayInstanceIdList": null,
                    "GatewayInstanceType": null,
                    "GroupContext": null,
                    "GroupId": "non-tsf-gateway-group",
                    "GroupName": "本地配置API",
                    "GroupType": null,
                    "NamespaceNameKey": null,
                    "NamespaceNameKeyPosition": "path",
                    "ServiceNameKey": null,
                    "ServiceNameKeyPosition": "path",
                    "Status": null,
                    "UpdatedTime": null
                },
                {
                    "AclMode": "none",
                    "ApiCount": 15,
                    "AuthType": "none",
                    "BindedGatewayDeployGroups": [],
                    "CreatedTime": "2024-12-23 01:29:13",
                    "Description": "",
                    "GatewayInstanceId": "gw-ins-b09khqjq",
                    "GatewayInstanceIdList": null,
                    "GatewayInstanceType": "none",
                    "GroupContext": "/ctx",
                    "GroupId": "grp-nb08ur29",
                    "GroupName": "grpName",
                    "GroupType": "ms",
                    "NamespaceNameKey": null,
                    "NamespaceNameKeyPosition": "path",
                    "ServiceNameKey": null,
                    "ServiceNameKeyPosition": "path",
                    "Status": "released",
                    "UpdatedTime": "2024-12-23 01:30:03"
                }
            ],
            "TotalCount": 2
        }
    }
}
```

