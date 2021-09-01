**Example 1: 获取设备的历史事件**



Input: 

```
tccli iotvideo DescribeDeviceEventHistory --cli-unfold-argument  \
    --ProductId QDA1PZLBNB \
    --DeviceName dev01 \
    --Type  \
    --EventId low_voltage \
    --StartTime 1560355200 \
    --EndTime 1601196327 \
    --Size 50
```

Output: 
```
{
    "Response": {
        "Listover": true,
        "RequestId": "3b64cf0b-c10e-4b4a-97a1-40ab7116b362",
        "EventHistory": [
            {
                "TimeStamp": 1561619346000,
                "ProductId": "QDA1PZLBNB",
                "DeviceName": "dev01",
                "EventId": "low_voltage",
                "Type": "alert",
                "Data": "{\"voltage\": 3.487172}"
            }
        ],
        "Total": 1,
        "Context": "DnF1ZXJ5VGhlbkZldGNoCgAAAAAAABO3FkI2SzRCVTJYUjZxUVRnbUJRaUJzc0EAAAAAAAATuBZCNks0QlUyWFI2cVFUZ21CUWlCc3NBAAAAAAAAE7kWQjZLNEJVMlhSNnFRVGdtQlFpQnNzQQAAAAAAABO6FkI2SzRCVTJYUjZxUVRnbUJRaUJzc0EAAAAAAAATuxZCNks0QlUyWFI2cVFUZ21CUWlCc3NBAAAAAAAAE7wWQjZLNEJVMlhSNnFRVGdtQlFpQnNzQQAAAAAAABO9FkI2SzRCVTJYUjZxUVRnbUJRaUJzc0EAAAAAAAATvhZCNks0QlUyWFI2cVFUZ21CUWlCc3NBAAAAAAAAE78WQjZLNEJVMlhSNnFRVGdtQlFpQnNzQQAAAAAAABPAFkI2SzRCVTJYUjZxUVRnbUJRaUJzc0E="
    }
}
```

