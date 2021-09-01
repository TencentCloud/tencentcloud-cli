**Example 1: 查询API分组**



Input: 

```
tccli tsf DescribeApiGroup --cli-unfold-argument  \
    --GroupId grp-e42d597
```

Output: 
```
{
    "Response": {
        "Result": {
            "Status": "xx",
            "UpdatedTime": "xx",
            "AuthType": "secret",
            "Description": "xx",
            "BindedGatewayDeployGroups": [
                {
                    "DeployGroupId": "grp-fdsfds",
                    "ApplicationName": "xx",
                    "GroupStatus": "drafted",
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
            "CreatedTime": "xx",
            "GroupId": "grp-dasdasdas"
        },
        "RequestId": "5d996e05507e42d5970cd2e25ed5267a"
    }
}
```

