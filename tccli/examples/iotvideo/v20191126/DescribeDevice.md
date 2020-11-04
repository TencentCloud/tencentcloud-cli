**Example 1: 获取设备信息**



Input: 

```
tccli iotvideo DescribeDevice --cli-unfold-argument  \
    --Tid xxx
```

Output: 
```
{
    "Response": {
        "Data": {
            "Tid": "xxx",
            "DeviceName": "test7W67W8G1NMJTQ",
            "ProductId": "453119049838",
            "ActiveTime": 0,
            "Disabled": false,
            "StreamStatus": false,
            "OtaVersion": "test",
            "Online": 0,
            "LastOnlineTime": 0,
            "Certificate": "AQEAAAAAAACO1mh5QphULMgBX5X0t0OK6+Z+xyyY3NRE+pkDapTQ0ECZd5PX6Qt9D3cq5JomqC63VdZ8Ca6Q0Dld9GWiKoCbQpOk46FPhGZVCoe7pR00QkyTntypyoYy",
            "WhiteBoxSoUrl": "http://tid-softreinforce-1256872341.cos.ap-guangzhou.myqcloud.com/libwbc_450971566142_82efa4dfd3237ba500181dbd538ab4a0.so",
            "IotModel": "xxx"
        },
        "RequestId": "9c90991d-9382-4016-91c3-b74c754cc18f"
    }
}
```

