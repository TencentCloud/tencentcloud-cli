**Example 1: 镜像仓库敏感信息列表导出**



Input: 

```
tccli tcss DescribeAssetImageRegistryRiskListExport --cli-unfold-argument  \
    --ExportField Path RiskLevel Category VirusName Tags \
    --Id 3421599
```

Output: 
```
{
    "Response": {
        "RequestId": "488e3711-8515-450a-9a40-df3e95c806fa",
        "DownloadUrl": "https://image-registory-1302977000.cos.ap-guangzhou.myqcloud.com/251011530-100015468030-ImageRiskListExport.csv?q-sign-algorithm=sha1&q-ak=AKIDSefQCiRPhjYAW4BR9b1B9qqd4E71a63k&q-sign-time=1611990834%3B1611990894&q-key-time=1611990834%3B1611990894&q-header-list=host&q-url-param-list=&q-signature=2736b65c910654d3d87b96b7c075e6d83a96f11d"
    }
}
```

