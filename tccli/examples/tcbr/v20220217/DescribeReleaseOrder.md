**Example 1: 查询发布单**



Input: 

```
tccli tcbr DescribeReleaseOrder --cli-unfold-argument  \
    --EnvId abc \
    --ServerName abc \
    --Status abc
```

Output: 
```
{
    "Response": {
        "IsExist": true,
        "ReleaseOrderInfo": {
            "Id": 0,
            "ServerName": "abc",
            "CurrentVersion": {
                "VersionName": "abc",
                "FlowRatio": 0,
                "Status": "abc",
                "CreatedTime": "abc",
                "UpdatedTime": "abc",
                "BuildId": 0,
                "UploadType": "abc",
                "Remark": "abc",
                "UrlParam": {
                    "Key": "abc",
                    "Value": "abc"
                },
                "Priority": 0,
                "IsDefaultPriority": true,
                "FlowParams": [
                    {
                        "Key": "abc",
                        "Value": "abc",
                        "Priority": 0
                    }
                ],
                "MinReplicas": 0,
                "MaxReplicas": 0,
                "RunId": "abc",
                "Percent": 0,
                "CurrentReplicas": 0,
                "Architecture": "abc"
            },
            "ReleaseVersion": {
                "VersionName": "abc",
                "FlowRatio": 0,
                "Status": "abc",
                "CreatedTime": "abc",
                "UpdatedTime": "abc",
                "BuildId": 0,
                "UploadType": "abc",
                "Remark": "abc",
                "UrlParam": {
                    "Key": "abc",
                    "Value": "abc"
                },
                "Priority": 0,
                "IsDefaultPriority": true,
                "FlowParams": [
                    {
                        "Key": "abc",
                        "Value": "abc",
                        "Priority": 0
                    }
                ],
                "MinReplicas": 0,
                "MaxReplicas": 0,
                "RunId": "abc",
                "Percent": 0,
                "CurrentReplicas": 0,
                "Architecture": "abc"
            },
            "GrayStatus": "abc",
            "ReleaseStatus": "abc",
            "TrafficTypeValues": [
                {
                    "Key": "abc",
                    "Value": "abc"
                }
            ],
            "TrafficType": "abc",
            "FlowRatio": 0,
            "CreateTime": "abc",
            "IsReleasing": true
        },
        "LastReleasedSuccessTime": "abc",
        "RequestId": "abc"
    }
}
```

