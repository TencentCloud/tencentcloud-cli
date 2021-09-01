**Example 1: 拉取生成包列表**

拉取生成包列表

Input: 

```
tccli gse DescribeAssets --cli-unfold-argument  \
    --AssetRegion ap-shanghai \
    --Limit 1 \
    --Offset 2 \
    --Filter xxx
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Assets": [
            {
                "AssetId": "asset-xxxxx",
                "AssetName": "test",
                "AssetVersion": "test",
                "OperateSystem": "centos",
                "Stauts": 1,
                "Size": "11M",
                "CreateTime": "2019-11-28 20:04:32",
                "BindFleetNum": 2,
                "AssetArn": "xx",
                "OsType": "CentOS",
                "ResourceType": "IMAGE",
                "SharingStatus": "SHARED",
                "ImageId": "xx"
            }
        ],
        "RequestId": "c7bfcad5-3f20-472f-9afc-13a66faebad8"
    }
}
```

