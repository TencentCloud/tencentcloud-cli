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
        "RequestId": "5d996e5507e42d5970cd2e25ed5267a",
        "Result": {
            "TotalCount": 30,
            "Content": [
                {
                    "UpdatedTime": "2021-03-17 10:44:27",
                    "PathMapping": "/pd/v1/echo",
                    "MicroserviceName": "服务名称",
                    "Description": "描述",
                    "MicroserviceId": "服务ID",
                    "NamespaceName": "命名空间名称",
                    "ApiId": "api-d5970cd2",
                    "UsableStatus": "enabled",
                    "ApiType": "ms",
                    "ReleaseStatus": "released",
                    "GroupName": "分组名称",
                    "Host": "xx",
                    "Method": "POST",
                    "RateLimitStatus": "disabled",
                    "Timeout": 0,
                    "NamespaceId": "命名空间ID",
                    "CreatedTime": "2021-03-17 10:44:27",
                    "Path": "/provider-demo/v1/echo",
                    "ReleasedTime": "2021-03-17 10:44:27",
                    "MockStatus": "disabled",
                    "GroupId": "grp-ib3xchsw"
                }
            ]
        }
    }
}
```

