**Example 1: 购买云存服务**



Input: 

```
tccli iotvideo CreateStorageService --cli-unfold-argument  \
    --PkgId xx \
    --ChnNum 123 \
    --EnableTime 0 \
    --OrderCount 112 \
    --AccessId xx \
    --Tid xx \
    --StorageRegion xx
```

Output: 
```
{
    "Response": {
        "RequestId": "43348837-a756-4939-92b6-77c333c1b96e",
        "IsRenew": true,
        "ServiceId": "000001010006aada08000000a68601800a000000a6860100",
        "StorageRegion": "ap-guangzhou",
        "Tid": "xxxx",
        "ChnNum": 0,
        "AccessId": "9223801559354179592",
        "StartTime": 1602664844,
        "EndTime": 1607935244,
        "Status": 1,
        "Data": [
            {
                "OrderId": 58,
                "PkgId": "yc1m3d",
                "Status": 2,
                "StartTime": 1602664844,
                "EndTime": 1605343244
            },
            {
                "OrderId": 59,
                "PkgId": "yc1m3d",
                "Status": 2,
                "StartTime": 1605343244,
                "EndTime": 1607935244
            }
        ]
    }
}
```

