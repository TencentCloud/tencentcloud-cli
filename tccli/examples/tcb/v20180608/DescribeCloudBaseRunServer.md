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
        "ServerName": "xx",
        "IsPublic": true,
        "ImageRepo": "xx",
        "TrafficType": "xx",
        "SourceType": "xx",
        "TotalCount": 0,
        "RequestId": "xx",
        "VersionItems": [
            {
                "Status": "xx",
                "UpdatedTime": "xx",
                "Remark": "xx",
                "VersionName": "xx",
                "BuildId": 0,
                "UploadType": "xx",
                "Priority": 0,
                "UrlParam": {
                    "Value": "xx",
                    "Key": "xx"
                },
                "FlowRatio": 0,
                "MinReplicas": 0,
                "IsDefaultPriority": true,
                "FlowParams": [
                    {
                        "Priority": 0,
                        "Value": "xx",
                        "Key": "xx"
                    }
                ],
                "CreatedTime": "xx",
                "MaxReplicas": 0
            }
        ]
    }
}
```

