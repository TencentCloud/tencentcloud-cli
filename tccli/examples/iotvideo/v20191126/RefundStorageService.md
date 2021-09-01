**Example 1: 退订已购买的云存服务**



Input: 

```
tccli iotvideo RefundStorageService --cli-unfold-argument  \
    --ServiceId xxxxxx \
    --OrderId 111
```

Output: 
```
{
    "Response": {
        "Status": 2,
        "ChnNum": 0,
        "AccessId": "xx",
        "ServiceId": "xx",
        "RequestId": "xx",
        "StartTime": 1602664760,
        "Tid": "xx",
        "EndTime": 1605343160,
        "Data": [
            {
                "OrderId": "xx",
                "PkgId": "xx",
                "EndTime": 0,
                "StartTime": 0,
                "Status": 0
            }
        ],
        "StorageRegion": "xx"
    }
}
```

