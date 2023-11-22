**Example 1: 获取审计实例列表**

无

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
        "RequestId": "43-12121-812w1221213-62usf9093",
        "Items": [
            {
                "BillingAmount": 0,
                "LowRealStorage": 0,
                "InstanceId": "cdb-euu5fkcj",
                "AuditTask": 1,
                "CreateAt": "2022-03-02 10:09:08",
                "AuditStatus": "1",
                "LogExpireDay": 1,
                "AuditAll": true,
                "InstanceInfo": {
                    "ProjectId": 0,
                    "TagList": [
                        {
                            "TagKey": "test",
                            "TagValue": "1"
                        }
                    ]
                },
                "HighRealStorage": 0,
                "HighLogExpireDay": 30,
                "LowLogExpireDay": 7
            }
        ]
    }
}
```

