**Example 1: ListCloudInstanceRegions**

查询云实例地域列表

Input: 

```
tccli wedata ListCloudInstanceRegions --cli-unfold-argument  \
    --ConnectionType TENCENT_MYSQL
```

Output: 
```
{
    "Response": {
        "Data": {
            "InstanceRegions": [
                {
                    "Region": "ap-guangzhou",
                    "RegionName": "华南地区(广州)"
                }
            ]
        },
        "RequestId": "c62ab2d8-4693-45b3-9f33-ab4a91cdc86b"
    }
}
```

