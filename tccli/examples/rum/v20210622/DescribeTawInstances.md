**Example 1: 查询 RUM 业务系统信息**

查询 RUM 业务系统信息

Input: 

```
tccli rum DescribeTawInstances --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "InstanceStatus": 0,
                "AreaId": 0,
                "Tags": [
                    {
                        "Key": "abc",
                        "Value": "abc"
                    }
                ],
                "InstanceId": "abc",
                "ClusterId": 0,
                "InstanceDesc": "abc",
                "ChargeStatus": 0,
                "ChargeType": 0,
                "UpdatedAt": "abc",
                "DataRetentionDays": 0,
                "InstanceName": "abc",
                "CreatedAt": "abc",
                "InstanceType": 0
            }
        ],
        "TotalCount": 0,
        "RequestId": "abc"
    }
}
```

