**Example 1: 查询实例信息**



Input: 

```
tccli cdb DescribeInstanceInfo --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "AddTimeStamp": "2025-10-14 14:51:37",
                "AppId": 251434123,
                "CdbMem": 4000,
                "CdbType": "CLOUD_NATIVE_CLUSTER",
                "CdbVip": "",
                "CdbVolume": 100,
                "CdbVport": 0,
                "Cpu": 2,
                "Deadline": "0001-01-01 00:00:00",
                "InstType": 1,
                "InstanceNodes": 2,
                "IsolateTimeStamp": "0001-01-01 00:00:00",
                "ModTimeStamp": "2025-10-14 14:51:37",
                "OssClusterId": 0,
                "ProjectId": 0,
                "ResourceId": "",
                "RouteName": "cdb1081853xx",
                "Status": 0,
                "UInstanceId": "cdb-44yrfxxx",
                "Vip": "10.0.x.x",
                "Vport": 3306
            }
        ],
        "TotalCount": 144,
        "RequestId": "9a873a27-bc6d-4b0e-8213-a20690157533"
    }
}
```

