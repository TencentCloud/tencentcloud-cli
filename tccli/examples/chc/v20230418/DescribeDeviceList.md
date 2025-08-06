**Example 1: 查询服务器设备列表**



Input: 

```
tccli chc DescribeDeviceList --cli-unfold-argument  \
    --DeviceType server
```

Output: 
```
{
    "Response": {
        "DeviceSet": [
            {
                "AssetId": "TH24122400001",
                "DeviceType": "server",
                "IdcId": 159,
                "IdcName": "天津数据备份中心东区DC",
                "IdcUnitId": 596,
                "IdcUnitName": "天津数据备份中心东区DC1栋M303",
                "Ip": "",
                "ModelVersion": "DELL R420-V2",
                "OnshelfDate": "2025-01-02",
                "PositionCode": 20,
                "PowerOnTime": "2025-01-02",
                "RackId": 15452,
                "RackName": "M303-C15",
                "ServerTypeId": 1,
                "Sn": "20241218chc0001",
                "Status": "POWER_OFF",
                "SvrIsSpecial": 0
            }
        ],
        "RequestId": "13e97f35-2559-4a69-a4ea-38c5d9f42c80",
        "Total": 2513
    }
}
```

