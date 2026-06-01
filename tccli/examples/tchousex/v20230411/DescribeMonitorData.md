**Example 1: 查询cos监控数据**

查询cos监控数据

Input: 

```
tccli tchousex DescribeMonitorData --cli-unfold-argument  \
    --GetMonitorDataRequest {
    "Namespace": "QCE/COS",
    "MetricName": "InternalTrafficBandwidth",
    "Instances": [
        {
            "Dimensions": [
                {
                    "Name": "bucket",
                    "Value": "warehouse-j5bbsmrs-1305504398"
                }
            ]
        }
    ],
    "Period": 300,
    "StartTime": "2024-11-05 17:21:26",
    "EndTime": "2024-11-05 18:21:26"
} \
    --ResourceAppId 1305504398 \
    --ResourceRegion ap-guangzhou
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "",
        "RequestId": "a029578e-c6ad-40c9-b303-522ea1c1393f",
        "ReturnData": "{\"Response\":{\"Period\":300,\"MetricName\":\"InternalTrafficBandwidth\",\"DataPoints\":[{\"Dimensions\":[{\"Name\":\"bucket\",\"Value\":\"warehouse-j5bbsmrs-1305504398\"}],\"Timestamps\":[1730798400,1730798700,1730799000,1730799300,1730799600,1730799900,1730800200,1730800500,1730800800,1730801100,1730801400,1730801700,1730802000],\"Values\":[0,0,0,0,0,0,0,0,56.56,0,0,0,0]}],\"StartTime\":\"2024-11-05 17:20:00\",\"EndTime\":\"2024-11-05 18:20:00\",\"RequestId\":\"34f0a3a9-83b5-4403-b67a-328f5d0826dd\"}}"
    }
}
```

