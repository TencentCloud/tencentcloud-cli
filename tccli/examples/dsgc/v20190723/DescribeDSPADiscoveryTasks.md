**Example 1: 获取分类分级任务列表**



Input: 

```
tccli dsgc DescribeDSPADiscoveryTasks --cli-unfold-argument  \
    --DataSourceType cdb \
    --DspaId dspa-001 \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "91c7a73v-e540-4780-8b8e-74e0b65b4f1a",
        "TotalCount": 1,
        "Items": [
            {
                "Name": "通用规则集测试",
                "Description": "",
                "Period": 0,
                "Plan": 0,
                "Enable": 1,
                "TimingStartTime": null,
                "GeneralRuleSetEnable": 0,
                "DataSourceInfo": {
                    "ResourceRegion": "ap-guangzhou",
                    "DataSourceId": "cdb-6dcpe42v",
                    "DataSourceName": "采集测试",
                    "ProxyAddress": null,
                    "Condition": "test_report,dsgctest001",
                    "DataSourceType": "cdb"
                },
                "ComplianceUpdate": false,
                "Result": {
                    "Id": 4142,
                    "EndTime": "2024-11-05 17:17:30",
                    "Status": 3,
                    "Result": ""
                }
            }
        ]
    }
}
```

