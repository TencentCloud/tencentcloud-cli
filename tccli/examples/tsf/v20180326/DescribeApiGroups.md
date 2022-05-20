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

**Example 2: test**



Input: 

```
tccli tsf DescribeApiGroups --cli-unfold-argument  \
    --Status 字符串 \
    --OrderBy 字符串 \
    --AuthType 字符串 \
    --OrderType 1 \
    --GroupType 字符串 \
    --Limit 1 \
    --GatewayInstanceId 字符串 \
    --SearchWord 字符串 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "RequestId": "685c0c8e-d107-44ed-bba0-723456e01783",
        "Result": null
    }
}
```

**Example 3: test1**



Input: 

```
tccli tsf DescribeApiGroups --cli-unfold-argument  \
    --Status 字符串 \
    --OrderBy 字符串 \
    --AuthType 字符串 \
    --OrderType 1 \
    --GroupType 字符串 \
    --Limit 1 \
    --GatewayInstanceId 字符串 \
    --SearchWord 字符串 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "RequestId": "a1deb916-ce41-4f0e-9307-deea50b14d44",
        "Result": null
    }
}
```

