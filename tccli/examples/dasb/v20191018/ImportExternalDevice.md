**Example 1: 导入外部资产信息**



Input: 

```
tccli dasb ImportExternalDevice --cli-unfold-argument  \
    --DeviceSet.0.Ip 1.1.1.1 \
    --DeviceSet.0.Name linux设备 \
    --DeviceSet.0.OsName Linux \
    --DeviceSet.0.Port 22
```

Output: 
```
{
    "Response": {
        "DeviceIdSet": [
            1,
            2,
            3
        ],
        "RequestId": "dfac9070-8b23-499e-83b2-a50e3ca059af"
    }
}
```

