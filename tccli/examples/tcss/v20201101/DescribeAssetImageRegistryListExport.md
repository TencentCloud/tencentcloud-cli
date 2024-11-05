**Example 1: 镜像仓库镜像列表导出**



Input: 

```
tccli tcss DescribeAssetImageRegistryListExport --cli-unfold-argument  \
    --ExportField InstanceName InstanceId RegistryType Namespace ImageName ImageTag ImageSize ImageDigest ImageId ImageRepoAddress ScanStatus VulCnt VirusCnt RiskCnt ScanStartTime ScanEndTime OsName IsAuthorized RegistryRegion
```

Output: 
```
{
    "Response": {
        "RequestId": "c00f4492-6973-4d8f-872b-c29d22c8eee0",
        "DownloadUrl": "https://download.url"
    }
}
```

