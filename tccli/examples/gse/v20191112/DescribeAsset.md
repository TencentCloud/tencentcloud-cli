**Example 1: 获取生成包信息**

获取生成包信息

Input: 

```
tccli gse DescribeAsset --cli-unfold-argument  \
    --AssetId asset-i5gtz5l9
```

Output: 
```
{
    "Response": {
        "Asset": {
            "AssetId": "build-xxxxx",
            "AssetName": "test",
            "AssetVersion": "test",
            "OperateSystem": "centos",
            "Stauts": 1,
            "Size": "11M",
            "CreateTime": "2019-11-28 20:04:32",
            "BindFleetNum": 2,
            "OsType": "xx",
            "ResourceType": "IMAGE",
            "SharingStatus": "SHARED",
            "AssetArn": "xx",
            "ImageId": "xx"
        },
        "RequestId": "c7bfcad5-3f20-472f-9afc-13a66faebad8"
    }
}
```

