**Example 1: 启用API**



Input: 

```
tccli tsf ChangeApiUsableStatus --cli-unfold-argument  \
    --ApiId api-m42wysh0 \
    --UsableStatus enabled
```

Output: 
```
{
    "Response": {
        "RequestId": "1e248975-03fa-4ce6-ab7b-71e022859221",
        "Result": {
            "ApiId": "api-m42wysh0",
            "ApiMatchType": "normal",
            "ApiType": "external",
            "CreatedTime": "2024-12-11 18:08:38",
            "Description": null,
            "GatewayDeployGroupId": null,
            "GroupId": "grp-h9xl5mmi",
            "GroupName": null,
            "Host": "http://test.com",
            "Md5": "39c57c50b244de7272311253edca3771",
            "Method": "GET",
            "MicroserviceId": "ms-external",
            "MicroserviceName": "ms-external",
            "MockStatus": "disabled",
            "NamespaceId": "namespace-external",
            "NamespaceName": "namespace-external",
            "Path": "/healthcheck",
            "PathMapping": "/health",
            "RateLimitStatus": null,
            "ReleaseStatus": "released",
            "ReleasedTime": null,
            "RpcExt": null,
            "RpcType": "http",
            "Timeout": null,
            "UpdatedTime": "2024-12-18 11:49:22",
            "UsableStatus": "enabled"
        }
    }
}
```

