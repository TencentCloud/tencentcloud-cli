**Example 1: 获取服务器舰队关联的资源**

删除服务器舰队时，可先访问该接口获取与服务器舰队关联的资源

Input: 

```
tccli gse DescribeFleetRelatedResources --cli-unfold-argument  \
    --FleetId fleet-qp3g3caa-nkeekxw6
```

Output: 
```
{
    "Response": {
        "RequestId": "2140e503-13cc-4249-af0f-b6ae0682ca18",
        "Resources": [
            {
                "ResourceId": "alias-qh85lwj6-k4bfes0u",
                "ResourceRegion": "ap-shanghai",
                "Type": "ALIAS"
            },
            {
                "ResourceId": "kongtest",
                "ResourceRegion": "ap-shanghai",
                "Type": "QUEUE"
            },
            {
                "ResourceId": "kongtest",
                "ResourceRegion": "na-siliconvalley",
                "Type": "QUEUE"
            }
        ]
    }
}
```

