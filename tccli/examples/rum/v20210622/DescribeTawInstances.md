**Example 1: 查询 RUM 业务系统信息**

查询 RUM 业务系统信息

Input: 

```
tccli rum DescribeTawInstances --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1 \
    --Filters.0.Name Region \
    --Filters.0.Values ap-guangzhou \
    --Filters.1.Name InstanceType \
    --Filters.1.Values 1
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "AreaId": 1,
                "ChargeStatus": 1,
                "ChargeType": 1,
                "ClusterId": 0,
                "CreatedAt": "2024-12-17 11:12:55",
                "DataRetentionDays": 30,
                "InstanceDesc": "test333",
                "InstanceId": "****GmpbKG4",
                "InstanceName": "test-333",
                "InstanceStatus": 2,
                "InstanceType": 1,
                "Tags": [
                    {
                        "Key": "二级业务",
                        "Value": "未分配业务_200003722"
                    }
                ],
                "UpdatedAt": "2024-12-18 18:22:01"
            }
        ],
        "RequestId": "8c3247ac-bafa-4e62-a73b-0b8c88e05202",
        "TotalCount": 1
    }
}
```

