**Example 1: 查询云存服务**



Input: 

```
tccli iotvideo DescribeStorageService --cli-unfold-argument  \
    --ServiceId 2300001383 \
    --GetFinishedOrder True
```

Output: 
```
{
    "Response": {
        "RequestId": "43348837-a756-4939-92b6-77c333c1b96e",
        "ServiceId": "000001010006aada08000000a68601800a000000a6860100",
        "StorageRegion": "ap-guangzhou",
        "Tid": "xxxx",
        "ChnNum": 0,
        "AccessId": "9223801559354179592",
        "StartTime": 1602664844,
        "EndTime": 1613292044,
        "Status": 1,
        "Data": [
            {
                "OrderId": 57,
                "PkgId": "yc1m3d",
                "Status": 4,
                "StartTime": 1602664760,
                "EndTime": 1605343160
            },
            {
                "OrderId": 58,
                "PkgId": "yc1m3d",
                "Status": 1,
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

