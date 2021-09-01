**Example 1: 描述作业配置接口示例**



Input: 

```
tccli oceanus DescribeResourceConfigs --cli-unfold-argument  \
    --ResourceId resource-iloy4wei
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "xx",
        "ResourceConfigSet": [
            {
                "Status": 0,
                "Remark": "xx",
                "CreatorUin": "xx",
                "ResourceType": 1,
                "ResourceId": "xx",
                "Region": "xx",
                "OwnerUin": "xx",
                "ResourceLoc": {
                    "StorageType": 1,
                    "Param": {
                        "Path": "xx",
                        "Region": "xx",
                        "Bucket": "xx"
                    }
                },
                "RefJobCount": 0,
                "Version": 1,
                "AppId": 1257051234,
                "CreateTime": "xx"
            }
        ]
    }
}
```

