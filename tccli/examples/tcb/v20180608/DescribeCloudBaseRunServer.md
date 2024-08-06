**Example 1: 查看某个服务的装填**



Input: 

```
tccli tcb DescribeCloudBaseRunServer --cli-unfold-argument  \
    --EnvId lotestapi100004 \
    --ServerName dockerservicename \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "ImageRepo": "tcb-100019615070-mjph/ca-znrdxowd_test-domain2",
        "IsPublic": false,
        "RequestId": "52855bd0-25cc-4294-913c-0b8ee0c65e76",
        "ServerName": "test-domain2",
        "SourceType": "custom",
        "TotalCount": 5,
        "TrafficType": "",
        "VersionItems": [
            {
                "VersionName": "test-domain2-009",
                "FlowRatio": 100,
                "Status": "normal",
                "CreatedTime": "2023-11-13 17:10:30",
                "UpdatedTime": "2023-11-13 17:41:00",
                "BuildId": 37196953,
                "UploadType": "package",
                "Remark": "",
                "UrlParam": null,
                "Priority": 0,
                "IsDefaultPriority": false,
                "FlowParams": null,
                "MinReplicas": 0,
                "MaxReplicas": 5,
                "RunId": "multi_tenant_1r2Sxhqf7GP3Mx",
                "Percent": 0,
                "CurrentReplicas": 0,
                "Architecture": ""
            }
        ]
    }
}
```

**Example 2: 查询单个云托管服务实例**

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
                "UrlParam": null,
                "VersionName": "envparam-001"
            }
        ]
    }
}
```

