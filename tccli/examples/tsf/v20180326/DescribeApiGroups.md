**Example 1: 查询API 分组信息列表**



Input: 

```
tccli tsf DescribeApiGroups --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20
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
                    "ApiCount": 0,
                    "GroupName": "xx",
                    "GroupContext": "xx",
                    "CreatedTime": "xx",
                    "GroupId": "xx"
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "5d996e05507e42d5970cd2e25ed5267a"
    }
}
```

