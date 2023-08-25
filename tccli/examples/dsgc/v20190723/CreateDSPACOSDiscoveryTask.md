**Example 1: 新增COS分类分级扫描任务**



Input: 

```
tccli dsgc CreateDSPACOSDiscoveryTask --cli-unfold-argument  \
    --DspaId dspa-001 \
    --Enable 0 \
    --Name 测试任务 \
    --ComplianceGroupIds 1 \
    --Bucket bucket_1 \
    --GeneralRuleSetEnable 0 \
    --Period 0 \
    --TimingStartTime xx \
    --FileSizeLimit 0 \
    --Plan 0 \
    --FileTypes .csv .txt \
    --DataSourceId xx \
    --Description xx \
    --ResourceRegion ap-guangzhou
```

Output: 
```
{
    "Response": {
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239",
        "TaskId": 1,
        "ResultId": 1
    }
}
```

