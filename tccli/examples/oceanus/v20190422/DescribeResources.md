**Example 1: 查询资源配置列表示例**



Input: 

```
tccli oceanus DescribeResources --cli-unfold-argument  \
    --ResourceIds resource-abd503yt
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "xx",
        "ResourceSet": [
            {
                "UpdateTime": "xx",
                "Name": "xx",
                "CreatorUin": "xx",
                "ResourceType": 1,
                "ResourceId": "xx",
                "Region": "xx",
                "OwnerUin": "xx",
                "Remark": "xx",
                "VersionCount": 0,
                "RefJobCount": 0,
                "LatestResourceConfigVersion": 1,
                "AppId": 1,
                "CreateTime": "xx",
                "ResourceLoc": {
                    "StorageType": 1,
                    "Param": {
                        "Path": "xx",
                        "Region": "xx",
                        "Bucket": "xx"
                    }
                }
            }
        ]
    }
}
```

