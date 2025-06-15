**Example 1: GetDeviceLocationHistory**

获取设备历史位置

Input: 

```
tccli iotexplorer GetDeviceLocationHistory --cli-unfold-argument  \
    --ProductId X4912BAIVR \
    --DeviceName dev1 \
    --StartTime 1604890314000 \
    --EndTime 1609890353000
```

Output: 
```
{
    "Response": {
        "Positions": [
            {
                "CreateTime": 1608882530000,
                "Longitude": 113.9709,
                "Latitude": 22.562782,
                "LocationType": "",
                "Accuracy": 42.3
            }
        ],
        "RequestId": "1e99faaf-a0f0-4c49-9d85-7f09f2b7f74e"
    }
}
```

