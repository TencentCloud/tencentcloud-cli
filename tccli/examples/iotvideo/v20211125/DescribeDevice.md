**Example 1: 查看设备详情**



Input: 

```
tccli iotvideo DescribeDevice --cli-unfold-argument  \
    --DeviceName test1 \
    --ProductId PTROMP3AOB
```

Output: 
```
{
    "Response": {
        "DeviceName": "test1",
        "DevicePsk": "awefwaef==",
        "EnableState": 1,
        "ExpireTime": 1657024055,
        "RequestId": "2172b7d1-9a49-4142-938a-ff4fa3d55881",
        "Online": 1,
        "LoginTime": 1608880525,
        "LogLevel": 1
    }
}
```

