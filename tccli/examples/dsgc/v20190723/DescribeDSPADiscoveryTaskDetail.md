**Example 1: 获取分类分级任务详情**



Input: 

```
tccli dsgc DescribeDSPADiscoveryTaskDetail --cli-unfold-argument  \
    --DspaId dspa-1f96daa1 \
    --TaskId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "91c7a73v-e540-4780-8b8e-74e0b65b4f1a",
        "Task": {
            "Name": "通用规则集",
            "Description": "这是通用规则集",
            "Period": 0,
            "Plan": 0,
            "Enable": 1,
            "TimingStartTime": "2022-10-21 10:12:20",
            "GeneralRuleSetEnable": 0,
            "DataSourceInfo": {
                "ResourceRegion": "ap-guangzhou",
                "DataSourceId": "cdb-6ddpe42v",
                "DataSourceName": "订单数据库",
                "ProxyAddress": [],
                "Condition": "test_report,dsgctest001",
                "DataSourceType": "cdb"
            },
            "CustomComplianceInfo": [
                {
                    "ComplianceGroupId": 1,
                    "ComplianceGroupName": "通用规则集"
                }
            ],
            "DefaultComplianceInfo": [
                {
                    "ComplianceGroupId": 1,
                    "ComplianceGroupName": "通用规则集"
                }
            ]
        }
    }
}
```

