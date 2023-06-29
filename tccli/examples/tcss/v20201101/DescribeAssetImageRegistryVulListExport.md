**Example 1: 镜像仓库漏洞列表导出**



Input: 

```
tccli tcss DescribeAssetImageRegistryVulListExport --cli-unfold-argument  \
    --ExportField CVEId POCId Name Components Category CategoryType Level Des OfficialSolution Reference DefenseSolution SubmitTime CVSS_Score CVSS_Desc \
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

