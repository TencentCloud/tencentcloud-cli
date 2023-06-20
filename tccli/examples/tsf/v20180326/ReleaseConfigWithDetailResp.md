**Example 1: 发布配置**

将一个应用配置项发布到指定的应用部署组

Input: 

```
tccli tsf ReleaseConfigWithDetailResp --cli-unfold-argument  \
    --ConfigId configId-xxxxxxx \
    --GroupId gourp-xxxxxx \
    --ReleaseDesc demo config realse
```

Output: 
```
{
    "Response": {
        "Result": {
            "ConfigReleaseId": "dcfgr-xxxxxx",
            "ConfigId": "null",
            "ConfigName": "null",
            "ConfigVersion": "null",
            "ReleaseTime": "null",
            "GroupId": "null",
            "GroupName": "null",
            "NamespaceId": "null",
            "NamespaceName": "null",
            "ClusterId": "null",
            "ClusterName": "null",
            "ReleaseDesc": "null",
            "ApplicationId": "null"
        },
        "RequestId": "36ccafba-c8ab-4d15-a4f1-4cfd2070d1d3"
    }
}
```

