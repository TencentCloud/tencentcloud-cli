**Example 1: 修改COS分类分级任务**



Input: 

```
tccli dsgc ModifyDSPACOSDiscoveryTask --cli-unfold-argument  \
    --DspaId xx \
    --Enable 0 \
    --Name xx \
    --ComplianceGroupIds 1 \
    --GeneralRuleSetEnable 0 \
    --Period 0 \
    --TimingStartTime xx \
    --FileSizeLimit 1000 \
    --TaskId 1 \
    --Plan 0 \
    --FileTypes .csv .txt \
    --Description xx
```

Output: 
```
{
    "Response": {
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239"
    }
}
```

