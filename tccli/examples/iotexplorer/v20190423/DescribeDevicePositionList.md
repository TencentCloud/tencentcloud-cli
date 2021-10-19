**Example 1: 获取设备位置列表**



Input: 

```
tccli iotexplorer DescribeDevicePositionList --cli-unfold-argument  \
    --ProductIdList X4912BAIVR \
    --CoordinateType 3 \
    --Offset 0 \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "Positions": [
            {
                "ProductId": "X4912BAIVR",
                "Items": [
                    {
                        "DeviceName": "dev1",
                        "CreateTime": 1600260759000,
                        "Longitude": 113.9709,
                        "Latitude": 22.562782
                    }
                ],
                "Total": 1
            }
        ],
        "RequestId": "f58e6eab-ffcb-425d-94ac-f14047d93609",
        "Total": 1
    }
}
```

