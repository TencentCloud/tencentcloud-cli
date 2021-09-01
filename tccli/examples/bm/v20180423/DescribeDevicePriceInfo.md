**Example 1: 查询服务器价格信息**



Input: 

```
tccli bm DescribeDevicePriceInfo --cli-unfold-argument  \
    --TimeUnit m \
    --TimeSpan 12 \
    --InstanceIds cpm-xxxxxxx1 cpm-xxxxxxx2
```

Output: 
```
{
    "Response": {
        "DevicePriceInfoSet": [
            {
                "InstanceId": "cpm-xxxxxxx1",
                "DeviceClassCode": "PS001v1",
                "IsElastic": 0,
                "CpmPayMode": 2,
                "CpuDescription": "E5-2620v3(6核)*2",
                "MemDescription": "64GB",
                "DiskDescription": "6*300G(SAS)",
                "NicDescription": "1G * 2",
                "GpuDescription": "",
                "RaidDescription": "支持",
                "Price": 337000,
                "NormalPrice": 0,
                "TotalCost": 4044000,
                "RealTotalCost": 2022000,
                "TimeSpan": 12,
                "TimeUnit": "m",
                "GoodsCount": 1
            },
            {
                "InstanceId": "cpm-xxxxxxx2",
                "DeviceClassCode": "PS001v1",
                "IsElastic": 0,
                "CpmPayMode": 2,
                "CpuDescription": "E5-2620v3(6核)*2",
                "MemDescription": "64GB",
                "DiskDescription": "6*300G(SAS)",
                "NicDescription": "1G * 2",
                "GpuDescription": "",
                "RaidDescription": "支持",
                "Price": 337000,
                "NormalPrice": 0,
                "TotalCost": 4044000,
                "RealTotalCost": 2022000,
                "TimeSpan": 12,
                "TimeUnit": "m",
                "GoodsCount": 1
            }
        ],
        "RequestId": "906e3948-0dd6-4eae-9583-3ad98e22ba61"
    }
}
```

