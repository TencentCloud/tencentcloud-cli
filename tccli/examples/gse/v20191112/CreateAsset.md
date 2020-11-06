**Example 1: 创建生成包**

创建生成包

Input: 

```
tccli gse CreateAsset --cli-unfold-argument  \
    --BucketKey GseLinuxServer.zip \
    --AssetName asset-demo \
    --AssetVersion 1.0 \
    --AssetRegion ap-shanghai \
    --OperateSystem CentOS7.16
```

Output: 
```
{
    "Response": {
        "AssetId": "asset-xxx",
        "AssetArn": "xx",
        "RequestId": "c7bfcad5-3f20-472f-9afc-13a66faebad8"
    }
}
```

