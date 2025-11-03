**Example 1: 查询该时间段、对应项目、设备的不同分辨率的通话时长汇总**



Input: 

```
tccli trro GetTotalDuration --cli-unfold-argument  \
    --StartTime 1680076919 \
    --EndTime 1688025719 \
    --ProjectId dadad \
    --DeviceId asdad
```

Output: 
```
{
    "Response": {
        "Voice": 0,
        "SD": 0,
        "HD": 3240,
        "FHD": 0,
        "TwoK": 0,
        "FourK": 0,
        "Online": 432,
        "RequestId": "17082975-0c65-503a-b249-ea27c34f8af9"
    }
}
```

