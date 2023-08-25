**Example 1: 创建资产梳理报告导出重试任务**

创建资产梳理报告导出重试任务

Input: 

```
tccli dsgc CreateAssetSortingReportRetryTask --cli-unfold-argument  \
    --ReportTaskId 1 \
    --DspaId abc
```

Output: 
```
{
    "Response": {
        "ReportTaskId": 1,
        "RequestId": "abc"
    }
}
```

