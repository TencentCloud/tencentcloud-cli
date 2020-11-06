**Example 1: 将已购买的云存服务转移到另一设备**



Input: 

```
tccli iotvideo DeliverStorageService --cli-unfold-argument  \
    --SrcServiceId 3452345 \
    --Tid 2345345 \
    --ChnNum 123 \
    --AccessId 4564545645
```

Output: 
```
{
    "Response": {
        "RequestId": "43348837-a756-4939-92b6-77c333c1b96e",
        "SrcServiceId": "000001010006aada08000000a68601800a000000a6860100",
        "ServiceId": "0000010100d641410b000000b086018004000000b0860100",
        "StorageRegion": "",
        "Tid": "xxxx",
        "ChnNum": 0,
        "AccessId": "9223801602303852555",
        "StartTime": 1602662040,
        "EndTime": 1605340416,
        "Status": 1,
        "Data": [
            {
                "OrderId": 56,
                "PkgId": "yc1m3d",
                "Status": 3,
                "StartTime": 1602662040,
                "EndTime": 1605340416
            }
        ]
    }
}
```

