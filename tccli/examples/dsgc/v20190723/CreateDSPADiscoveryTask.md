**Example 1: 新增分类分级任务**



Input: 

```
tccli dsgc CreateDSPADiscoveryTask --cli-unfold-argument  \
    --Enable 1 \
    --Name 分类分级任务 \
    --ComplianceGroupIds 0 \
    --DataSourceType 1 \
    --GeneralRuleSetEnable 1 \
    --Period 0 \
    --TimingStartTime 2021-11-11 10:46:18 \
    --DspaId dspa-ab50f3b1 \
    --DataSourceId cdb-6cmpe42v \
    --Plan 0 \
    --ResourceRegion ap-guangzhou \
    --Condition db1,db_2 \
    --Description 分类分级扫描任务
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

