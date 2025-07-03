**Example 1: 获取审计实例列表**

获取审计实例列表

Input: 

```
tccli cdb DescribeAuditInstanceList --cli-unfold-argument  \
    --AuditMode 0 \
    --Limit 1 \
    --Filters.0.Values cdb-euu5fkcj \
    --Filters.0.Name InstanceId \
    --Filters.0.ExactMatch True \
    --AuditSwitch 0 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Items": [
            {
                "InstanceId": "cdb-euu5fkcj",
                "AuditStatus": "OFF",
                "AuditTask": 1,
                "LogExpireDay": 1,
                "HighLogExpireDay": 1,
                "LowLogExpireDay": 1,
                "BillingAmount": 0,
                "HighRealStorage": 0,
                "LowRealStorage": 0,
                "AuditAll": true,
                "CreateAt": "2022-03-02 10:09:08",
                "InstanceInfo": {
                    "ProjectId": 0,
                    "TagList": [
                        {
                            "TagKey": "andy",
                            "TagValue": "1"
                        }
                    ],
                    "DbType": "MYSQL",
                    "DbVersion": "5.7"
                },
                "RealStorage": 0,
                "OldRule": true,
                "RuleTemplateIds": [
                    "cdb-art-nuf7ej8d"
                ]
            }
        ],
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

