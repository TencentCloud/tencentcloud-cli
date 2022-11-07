**Example 1: 查询存储桶地域列表**



Input: 

```
tccli vod DescribeStorageRegions --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "requestId",
        "StorageRegionInfos": [
            {
                "Region": "ap-chongqing",
                "Description": "重庆",
                "Status": "opened",
                "IsDefault": true,
                "Area": "Chinese Mainland"
            }
        ]
    }
}
```

