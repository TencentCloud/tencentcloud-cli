**Example 1: 查询API分组下的Api列表信息**



Input: 

```
tccli tsf DescribeGatewayApis --cli-unfold-argument  \
    --GroupId grp-nb08ur29 \
    --SearchWord /swagger \
    --Offset 0 \
    --Limit 5 \
    --GatewayDeployGroupId group-yd3b588a \
    --ReleaseStatus released
```

Output: 
```
{
    "Response": {
        "RequestId": "223e1309-700b-47be-bbc6-cddcc510ece4",
        "Result": {
            "Content": [
                {
                    "ApiId": "api-1eqe6556",
                    "ApiMatchType": "normal",
                    "ApiType": "ms",
                    "CreatedTime": "2024-12-23 01:29:41",
                    "Description": null,
                    "GatewayDeployGroupId": null,
                    "GroupId": "grp-nb08ur29",
                    "GroupName": null,
                    "Host": null,
                    "Md5": "c35e5178b28d1844054982d61481912e",
                    "Method": "GET",
                    "MicroserviceId": "ms-ba2jlxvk",
                    "MicroserviceName": "provider-demo",
                    "MockStatus": "disabled",
                    "NamespaceId": "namespace-qab7bq9v",
                    "NamespaceName": "shedfree_default",
                    "Path": "/swagger/getMessageBoxAddress",
                    "PathMapping": null,
                    "RateLimitStatus": null,
                    "ReleaseStatus": "released",
                    "ReleasedTime": null,
                    "RpcExt": null,
                    "RpcType": "http",
                    "Timeout": null,
                    "UpdatedTime": "2024-12-23 01:30:03",
                    "UsableStatus": "enabled"
                }
            ],
            "TotalCount": 7
        }
    }
}
```

