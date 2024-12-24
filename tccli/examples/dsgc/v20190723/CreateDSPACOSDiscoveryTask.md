**Example 1: CreateDSPACOSDiscoveryTask输入输出示例**



Input: 

```
tccli dsgc CreateDSPACOSDiscoveryTask --cli-unfold-argument  \
    --DspaId dspa-ab50dca1 \
    --Name 对象存储扫描任务 \
    --Enable 1 \
    --Period 0 \
    --Plan 0 \
    --ComplianceGroupIds 13108 \
    --FileSizeLimit 102400 \
    --Bucket cos-test \
    --DataSourceId cos-d653b \
    --ResourceRegion ap-guangzhou \
    --FileTypes .txt
```

Output: 
```
{
    "Response": {
        "RequestId": "1eb522ff-0d62-45f6-ae15-11f801e42673",
        "TaskId": 14253,
        "ResultId": 4146
    }
}
```

