**Example 1: 获取生成包支持的操作系统列表**

获取生成包支持的操作系统列表

Input: 

```
tccli gse DescribeAssetSystems --cli-unfold-argument  \
    --OsType Windows \
    --OsBit 64
```

Output: 
```
{
    "Response": {
        "AssetSupportSys": [
            {
                "ImageId": "img-xxx",
                "OsBit": "64",
                "OsType": "Windows",
                "OsVersion": "Windows Server 2012 R2 数据中心版 64位英文版"
            }
        ],
        "RequestId": "c7bfcad5-3f20-472f-9afc-13a66faebad8"
    }
}
```

