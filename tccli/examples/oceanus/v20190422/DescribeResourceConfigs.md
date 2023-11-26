**Example 1: 查询资源版本**

查询资源版本

Input: 

```
tccli oceanus DescribeResourceConfigs --cli-unfold-argument  \
    --ResourceId resource-qreuon9y \
    --Limit 1 \
    --WorkSpaceId space-53rqk422
```

Output: 
```
{
    "Response": {
        "RequestId": "d20bc7a4-8382-42d1-8f8b-91ec83eac1d5",
        "ResourceConfigSet": [
            {
                "AppId": 1257058945,
                "CreateTime": "2023-11-20 15:05:56",
                "CreatorUin": "100032489861",
                "OwnerUin": "100006386216",
                "RefJobCount": 0,
                "RefJobStatusCountSet": [],
                "Region": "ap-guangzhou",
                "Remark": "test",
                "ResourceId": "resource-qreuon9y",
                "ResourceLoc": {
                    "Param": {
                        "Bucket": "oceanus-online-resource01-gz-1257058918",
                        "Path": "1257058945/100006386216/upload/20231120150319/flink-hello-world-1.0.0.jar",
                        "Region": "ap-guangzhou"
                    },
                    "StorageType": 1
                },
                "ResourceType": 1,
                "Status": 1,
                "Version": 3
            }
        ],
        "TotalCount": 3
    }
}
```

