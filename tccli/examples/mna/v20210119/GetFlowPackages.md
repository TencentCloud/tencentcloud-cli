**Example 1: 示例1**



Input: 

```
tccli mna GetFlowPackages --cli-unfold-argument  \
    --ResourceId 56d11777-50f7-4c60-9c89-e7076c8529a9-0 \
    --DeviceId mna-test1 \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "PackageList": [
            {
                "ResourceId": "56d11777-50f7-4c60-9c89-e7076c8529a9-0",
                "AppId": 1,
                "PackageType": "DEVICE_1_FLOW_20G",
                "Status": 1,
                "ActiveTime": 1697181612,
                "ExpireTime": 1699860012,
                "DeviceList": [
                    "mna-test1",
                    "mna-test2"
                ],
                "CapacitySize": 20000,
                "CapacityRemain": 10000,
                "RenewFlag": true,
                "ModifyStatus": 0,
                "TruncFlag": false
            }
        ],
        "RequestId": "1206563f-f13f-4647-aaa8-37fa86954cc4-1"
    }
}
```

