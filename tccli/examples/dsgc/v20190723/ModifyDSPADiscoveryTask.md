**Example 1: 修改分类分级任务**



Input: 

```
tccli dsgc ModifyDSPADiscoveryTask --cli-unfold-argument  \
    --Enable 1 \
    --Name task \
    --ComplianceGroupIds 0 \
    --GeneralRuleSetEnable 1 \
    --Period 0 \
    --TimingStartTime 2021/4/2 10:46:18 \
    --DspaId dspa-0001 \
    --DataSourceId 123 \
    --Plan 0 \
    --TaskId 1 \
    --Condition db1,db_2 \
    --Description 扫描任务
```

Output: 
```
{
    "Response": {
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239"
    }
}
```

