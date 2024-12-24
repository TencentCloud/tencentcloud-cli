**Example 1: 修改COS分类分级任务**



Input: 

```
tccli dsgc ModifyDSPACOSDiscoveryTask --cli-unfold-argument  \
    --DspaId dspa-a1b2c3 \
    --Enable 0 \
    --Name 北京cos-csv扫描 \
    --ComplianceGroupIds 1 \
    --GeneralRuleSetEnable 0 \
    --Period 0 \
    --TimingStartTime 2022-09-10 00:00:00 \
    --FileSizeLimit 1000 \
    --TaskId 1 \
    --Plan 0 \
    --FileTypes .csv .txt \
    --Description 北京cos-csv扫描
```

Output: 
```
{
    "Response": {
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239"
    }
}
```

