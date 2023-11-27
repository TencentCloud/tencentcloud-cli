**Example 1: 查询资源**



Input: 

```
tccli oceanus DescribeResources --cli-unfold-argument  \
    --ResourceIds resource-qreuon9y \
    --Offset 0 \
    --Limit 0 \
    --WorkSpaceId space-53rqk422
```

Output: 
```
{
    "Response": {
        "RequestId": "2f1a8e8b-a5e7-41a1-a96c-f40091d6ffff",
        "ResourceSet": [
            {
                "AppId": 1257058945,
                "CreateTime": "2023-08-16 20:29:58",
                "CreatorUin": "100032489861",
                "FileName": "flink-hello-world-1.0.0.jar",
                "LatestResourceConfigVersion": 1,
                "Name": "flink-hello-world-1.0.0.jar",
                "OwnerUin": "100006386216",
                "RefJobCount": 2,
                "IsJobRun": 0,
                "RefJobStatusCountSet": [
                    {
                        "Count": 1,
                        "JobStatus": 5
                    },
                    {
                        "Count": 3,
                        "JobStatus": 4
                    }
                ],
                "Region": "ap-guangzhou",
                "Remark": "test",
                "ResourceId": "resource-qreuon9y",
                "ResourceLoc": {
                    "Param": {
                        "Bucket": "oceanus-online-resource01-gz-1257058918",
                        "Path": "1257058945/100006386216/upload/20230816202945/flink-hello-world-1.0.0.jar",
                        "Region": "ap-guangzhou"
                    },
                    "StorageType": 1
                },
                "ResourceType": 1,
                "UpdateTime": "2023-08-16 20:29:58",
                "VersionCount": 1,
                "WorkSpaceId": 2892
            }
        ],
        "TotalCount": 1
    }
}
```

