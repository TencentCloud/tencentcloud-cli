**Example 1: 示例**



Input: 

```
tccli mna GetFlowPackages --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 1
```

Output: 
```
{
    "Response": {
        "PackageList": [
            {
                "ActiveTime": 1734613941,
                "AppId": 251198806,
                "CapacityRemain": 50000,
                "CapacityRemainPrecise": 50000,
                "CapacitySize": 50000,
                "CreateTime": 1734613920,
                "DeviceList": [
                    "mna-6t5t54hcry",
                    "mna-s72mu68gh3"
                ],
                "ExpireTime": 1737292340,
                "ModifyStatus": 0,
                "PackageType": "DEVICE_2_FLOW_50G",
                "RenewFlag": true,
                "ResourceId": "live-jjc000eABvgr_qt",
                "Status": 1,
                "TruncFlag": false
            }
        ],
        "RequestId": "e6972818-74b2-4228-a5ec-70c11e37fe6c",
        "Total": 506
    }
}
```

