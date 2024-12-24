**Example 1: 获取COS分类分级任务详情**



Input: 

```
tccli dsgc DescribeDSPACOSDiscoveryTaskDetail --cli-unfold-argument  \
    --DspaId dspa-01 \
    --TaskId 123
```

Output: 
```
{
    "Response": {
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239",
        "Task": {
            "Name": "COS-YmY0MDA3-对应评估任务-存储桶未开启版本控制功能",
            "Description": "对象存储扫描",
            "Period": 0,
            "Plan": 0,
            "Enable": 1,
            "DataSourceInfo": {
                "ResourceRegion": "ap-guangzhou",
                "DataSourceId": "cos-d653b75c5bac583e5003012eff6cf40ecbadfe3c",
                "DataSourceName": "kyrie-cos-test-251007922",
                "ProxyAddress": null,
                "Condition": {
                    "Bucket": "kyrie-cos-test-251007922",
                    "FileTypes": [
                        ".txt",
                        ".pgm",
                        ".jpeg",
                        ".jp2",
                        ".webp",
                        ".pbm",
                        ".hdr",
                        ".xml",
                        ".doc",
                        ".xlsx",
                        ".html",
                        ".pdf",
                        ".pnm",
                        ".docx",
                        ".xls",
                        ".pptx",
                        ".jpg",
                        ".jpe",
                        ".csv",
                        ".log",
                        ".json",
                        ".tiff",
                        ".png",
                        ".bmp",
                        ".ppm"
                    ],
                    "FileSizeLimit": 1000
                }
            },
            "GeneralRuleSetEnable": 0,
            "CustomComplianceInfo": [
                {
                    "ComplianceGroupId": 1,
                    "ComplianceGroupName": "通用规则集"
                }
            ],
            "DefaultComplianceInfo": null,
            "TimingStartTime": null
        }
    }
}
```

