**Example 1: 查询设备类工单详情**



Input: 

```
tccli chc DescribeDeviceWorkOrderDetail --cli-unfold-argument  \
    --OrderId ord-25022518110325063
```

Output: 
```
{
    "Response": {
        "BaseInfo": {
            "DeviceType": "server",
            "IdcId": 373,
            "IdcName": "天津数据备份中心东区3栋DC",
            "IsPowerOffConfirm": "1",
            "Remark": "",
            "StuffOption": "2"
        },
        "DeviceSet": [
            {
                "AssetId": "TH2502250006E",
                "DeviceType": "server",
                "IdcId": 373,
                "IdcName": "天津数据备份中心东区3栋DC",
                "IdcUnitId": 2559,
                "IdcUnitName": "天津数据备份中心东区3栋DCM204",
                "PositionCode": 4,
                "RackName": "M204-J10",
                "Sn": "lihwli10225011"
            },
            {
                "AssetId": "TH2502250006D",
                "DeviceType": "server",
                "IdcId": 373,
                "IdcName": "天津数据备份中心东区3栋DC",
                "IdcUnitId": 2559,
                "IdcUnitName": "天津数据备份中心东区3栋DCM204",
                "PositionCode": 3,
                "RackName": "M204-J10",
                "Sn": "lihwli10225012"
            }
        ],
        "OrderId": "ord-25022518110325063",
        "OrderStatus": "finish",
        "OrderType": "rackOff",
        "RequestId": "c03f33b4-e3e3-4c22-9af3-e8791cee35df",
        "ServiceType": "rackOff",
        "StepSet": [
            {
                "FinishTime": "2025-02-25 18:11:03",
                "OwnerName": "godwin2@test.com",
                "StepName": "发起申请",
                "StepStatus": "finish"
            },
            {
                "FinishTime": "2025-02-25 18:12:05",
                "OwnerName": "",
                "StepName": "数经审核",
                "StepStatus": "finish"
            },
            {
                "FinishTime": "2025-02-25 18:18:07",
                "OwnerName": "",
                "StepName": "现场实施",
                "StepStatus": "finish"
            }
        ]
    }
}
```

