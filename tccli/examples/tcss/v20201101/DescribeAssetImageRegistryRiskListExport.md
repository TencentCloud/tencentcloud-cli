**Example 1: 镜像仓库敏感信息列表导出**



Input: 

```
tccli tcss DescribeAssetImageRegistryRiskListExport --cli-unfold-argument  \
    --ExportField Path RiskLevel Category VirusName Tags \
    --Id 123
```

Output: 
```
{
    "Response": {
        "RequestId": "488e3711-8515-450a-9a40-df3e95c806fa",
        "DownloadUrl": "https://xxx"
    }
}
```

