**Example 1: 查询API分组下的Api列表信息**



Input: 

```
tccli tsf DescribeGatewayApis --cli-unfold-argument  \
    --GroupId grp-5yk7oor1 \
    --GatewayDeployGroupId group-e42d597 \
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
                    "ApiId": "abc",
                    "NamespaceId": "abc",
                    "NamespaceName": "abc",
                    "MicroserviceId": "abc",
                    "MicroserviceName": "abc",
                    "Path": "abc",
                    "PathMapping": "abc",
                    "Method": "abc",
                    "GroupId": "abc",
                    "UsableStatus": "abc",
                    "ReleaseStatus": "abc",
                    "RateLimitStatus": "abc",
                    "MockStatus": "abc",
                    "CreatedTime": "abc",
                    "UpdatedTime": "abc",
                    "ReleasedTime": "abc",
                    "GroupName": "abc",
                    "Timeout": 0,
                    "Host": "abc",
                    "ApiType": "abc",
                    "Description": "abc",
                    "ApiMatchType": "abc",
                    "RpcExt": "abc",
                    "GatewayDeployGroupId": "abc",
                    "Md5": "abc",
                    "RpcType": "abc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

