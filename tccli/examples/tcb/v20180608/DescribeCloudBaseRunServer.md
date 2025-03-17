**Example 1: 查询单个云托管服务实例**

查询单个云托管服务实例

Input: 

```
tccli tcb DescribeCloudBaseRunServer --cli-unfold-argument  \
    --EnvId pre-tenant-4g9db6fj62889354 \
    --ServerName envparam \
    --Offset 0 \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "ImageRepo": "tcb-100019615070-mjph/ca-znrdxowd_envparam",
        "IsPublic": false,
        "RequestId": "0a14bef2-57d8-4d74-9d54-c0850e5395b3",
        "ServerName": "envparam",
        "SourceType": "custom",
        "Tag": "",
        "TotalCount": 1,
        "TrafficType": "",
        "VersionItems": [
            {
                "Architecture": "",
                "BuildId": 41355587,
                "CreatedTime": "2024-04-03 13:12:39",
                "CurrentReplicas": 0,
                "FlowParams": null,
                "FlowRatio": 100,
                "IsDefaultPriority": false,
                "MaxReplicas": 5,
                "MinReplicas": 0,
                "Percent": 0,
                "Priority": 0,
                "Remark": "",
                "RunId": "multi_tenant_1rrsvOvTuxr1La",
                "Status": "normal",
                "UpdatedTime": "2024-04-03 13:43:14",
                "UploadType": "repository",
                "UrlParam": {
                    "Key": "url1",
                    "Value": "value1"
                },
                "VersionName": "envparam-001"
            }
        ]
    }
}
```

