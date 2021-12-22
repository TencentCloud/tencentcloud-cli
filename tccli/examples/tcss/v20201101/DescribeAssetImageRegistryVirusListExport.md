**Example 1: 镜像仓库木马信息列表导出**



Input: 

```
tccli tcss DescribeAssetImageRegistryVirusListExport --cli-unfold-argument  \
    --ExportField Path RiskLevel Category VirusName Tags \
    --Id 123
```

Output: 
```
{
    "Response": {
        "RequestId": "62e5c0e8-2cae-410a-8240-9cefbd419e08",
        "DownloadUrl": "https://xxx"
    }
}
```

