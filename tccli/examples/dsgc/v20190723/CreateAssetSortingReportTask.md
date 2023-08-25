**Example 1: 创建资产梳理报表导出任务**

创建资产梳理报表导出任务

Input: 

```
tccli dsgc CreateAssetSortingReportTask --cli-unfold-argument  \
    --DspaId abc \
    --ComplianceId 1 \
    --AssetList.0.DataSourceType abc \
    --AssetList.0.DataSourceInfo.0.DataSourceId abc \
    --AssetList.0.DataSourceInfo.0.BindList abc
```

Output: 
```
{
    "Response": {
        "RequestId": "128009ac-7df4-0530-cc92-52f0d945e191",
        "ReportTaskId": 3
    }
}
```

