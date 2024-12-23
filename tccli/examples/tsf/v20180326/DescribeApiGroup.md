**Example 1: 查询API分组**



Input: 

```
tccli tsf DescribeApiGroup --cli-unfold-argument  \
    --GroupId grp-ptrhio2l
```

Output: 
```
{
    "Response": {
        "RequestId": "32429659-3422-48be-aad2-93930c7abdaf",
        "Result": {
            "AclMode": "none",
            "ApiCount": 4,
            "AuthType": "none",
            "BindedGatewayDeployGroups": [],
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
    }
}
```

