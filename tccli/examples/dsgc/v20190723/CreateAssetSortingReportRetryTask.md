**Example 1: 创建资产梳理报告导出重试任务**

创建资产梳理报告导出重试任务

Input: 

```
tccli dsgc CreateAssetSortingReportRetryTask --cli-unfold-argument  \
    --ReportTaskId 1 \
    --DspaId dspa-12ab34dc
```

Output: 
```
{
    "Response": {
        "ReportTaskId": 1,
        "RequestId": "91c7a73v-e540-4780-8b8e-74e0b65b4f1a"
    }
}
```

