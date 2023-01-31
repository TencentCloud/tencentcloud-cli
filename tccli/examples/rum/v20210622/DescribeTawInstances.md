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
                "AreaId": "1",
                "ChargeStatus": 1,
                "ChargeType": 1,
                "ClusterId": "1",
                "CreatedAt": "2021-04-29 20:51:05",
                "DataRetentionDays": "30",
                "InstanceDesc": "",
                "InstanceId": "taw-VJ2mHDEb",
                "InstanceName": "test",
                "InstanceStatus": 2,
                "Tags": [],
                "UpdatedAt": "2021-04-29 20:51:05"
            },
            {
                "AreaId": "1",
                "ChargeStatus": 1,
                "ChargeType": 1,
                "ClusterId": "1",
                "CreatedAt": "2021-04-29 20:59:15",
                "DataRetentionDays": "30",
                "InstanceDesc": "",
                "InstanceId": "taw-mE08H4Ez",
                "InstanceName": "test",
                "InstanceStatus": 2,
                "Tags": [],
                "UpdatedAt": "2021-04-29 20:59:15"
            }
        ],
        "RequestId": "d356e035-ac3d-4237-add9-50a44c01dd39",
        "TotalCount": "2"
    }
}
```

