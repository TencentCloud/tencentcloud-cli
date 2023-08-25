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
            "Name": "敏感数据测试",
            "Description": "test",
            "Period": 0,
            "Plan": 0,
            "Enable": 1,
            "TimingStartTime": null,
            "GeneralRuleSetEnable": 1,
            "CustomComplianceInfo": null,
            "DefaultComplianceInfo": [
                {
                    "ComplianceGroupId": 1,
                    "ComplianceGroupName": "default"
                }
            ]
        }
    }
}
```

