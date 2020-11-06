**Example 1: 请求示例**



Input: 

```
tccli redis DescribeInstanceDTSInfo --cli-unfold-argument  \
    --InstanceId crs-6ia1c1c3
```

Output: 
```
{
    "Response": {
        "CutDownTime": "2019-08-16 17:10:13",
        "DstInfo": {
            "InstanceId": "crs-jufvqtt7",
            "InstanceName": "dtsdsttest28",
            "RegionId": 1,
            "SetId": 15005,
            "Status": 1,
            "Type": 2,
            "Vip": "172.16.16.48",
            "ZoneId": 100002
        },
        "JobId": "dts-l2g434lt",
        "JobName": "redis_dts_test28",
        "Offset": 0,
        "RequestId": "f5ff1c8e-7ea4-40a8-b179-8a99c6f7085b",
        "SrcInfo": {
            "InstanceId": "crs-6ia1c1c3",
            "InstanceName": "dtsSrctest28",
            "RegionId": 1,
            "SetId": 15005,
            "Status": -4,
            "Type": 2,
            "Vip": "172.16.16.9",
            "ZoneId": 100002
        },
        "Status": 10,
        "StatusDesc": "已失败"
    }
}
```

