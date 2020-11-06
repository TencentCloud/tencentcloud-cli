**Example 1: 查询托管设备带外信息**



Input: 

```
tccli bm DescribeHostedDeviceOutBandInfo --cli-unfold-argument  \
    --ZoneId ap-shanghai-bls-2 \
    --InstanceIds chm-xxx0 chm-xxx1
```

Output: 
```
{
    "Response": {
        "HostedDeviceOutBandInfoSet": [
            {
                "InstanceId": "chm-xxx0",
                "OutBandIp": "100.81.160.26",
                "VpnIp": "139.199.40.96",
                "VpnPort": 443
            },
            {
                "InstanceId": "chm-xxx1",
                "OutBandIp": "100.81.160.43",
                "VpnIp": "139.199.40.96",
                "VpnPort": 443
            }
        ],
        "RequestId": "b6fe718b-3900-4fd9-b92d-ed463959e3b5"
    }
}
```

