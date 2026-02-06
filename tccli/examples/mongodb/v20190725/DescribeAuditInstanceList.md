**Example 1: 查询审计实例列表**



Input: 

```
tccli mongodb DescribeAuditInstanceList --cli-unfold-argument  \
    --AuditSwitch 1 \
    --Filters.0.Name InstanceId \
    --Filters.0.Values cmgo-f4twtt** \
    --AuditMode 0
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "AuditAll": true,
                "AuditStatus": "ON",
                "AuditTask": 1,
                "BillingAmount": 0,
                "CreateAt": "2025-10-23 14:39:03",
                "Deliver": "OFF",
                "DeliverSummary": [],
                "HighLogExpireDay": 7,
                "HighRealStorage": 0,
                "InstanceId": "cmgo-f4twtt**",
                "InstanceInfo": {
                    "AuditLogExpireDay": 0,
                    "AuditStatus": "OFF",
                    "InstanceId": "cmgo-f4twttpp",
                    "InstanceName": "levi_test",
                    "InstanceRole": "MASTER",
                    "InstanceType": "REPLICATE",
                    "MongodbVersion": "4.4 WT",
                    "ProjectId": 0,
                    "Region": "ap-guangzhou",
                    "Status": "running",
                    "SupportAudit": true,
                    "TagList": [
                        {
                            "TagKey": "suri",
                            "TagValue": "111111"
                        }
                    ],
                    "Zone": "ap-guangzhou-3"
                },
                "LogExpireDay": 1825,
                "LowLogExpireDay": 1818,
                "LowRealStorage": 0,
                "OldRule": false,
                "RealStorage": 0,
                "RuleTemplateIds": []
            }
        ],
        "RequestId": "f09d8d49-62d7-4409-b55a-31f58d6db015",
        "TotalCount": 1
    }
}
```

