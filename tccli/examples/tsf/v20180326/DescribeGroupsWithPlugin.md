**Example 1: 查询插件未绑定的分组列表**



Input: 

```
tccli tsf DescribeGroupsWithPlugin --cli-unfold-argument  \
    --PluginId pgn-iuyb0s7c \
    --Bound True \
    --SearchWord /grpCtx \
    --Offset 0 \
    --Limit 5 \
    --GatewayInstanceId gw-ins-4qvyt5dc
```

Output: 
```
{
    "Response": {
        "RequestId": "665d9f05-3e80-464f-beb0-64345fe5c61e",
        "Result": {
            "Content": [
                {
                    "AclMode": "none",
                    "ApiCount": 0,
                    "AuthType": "secret",
                    "BindedGatewayDeployGroups": [],
                    "CreatedTime": "2024-11-04 14:21:53",
                    "Description": "",
                    "GatewayInstanceId": "gw-ins-4qvyt5dc",
                    "GatewayInstanceIdList": null,
                    "GatewayInstanceType": null,
                    "GroupContext": "/grpCtx",
                    "GroupId": "grp-v446jrhc",
                    "GroupName": "grpName",
                    "GroupType": "ms",
                    "NamespaceNameKey": null,
                    "NamespaceNameKeyPosition": "path",
                    "ServiceNameKey": null,
                    "ServiceNameKeyPosition": "path",
                    "Status": "drafted",
                    "UpdatedTime": "2024-11-04 14:24:41"
                }
            ],
            "TotalCount": 1
        }
    }
}
```

