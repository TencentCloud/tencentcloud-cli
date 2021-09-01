**Example 1: 获取设备录像日期列表**



Input: 

```
tccli iotvideoindustry GetRecordDatesByDev --cli-unfold-argument  \
    --DeviceId device01 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Dates": [
            "2020-12-18",
            "2020-12-19",
            "2020-12-20",
            "2020-12-21",
            "2020-12-22"
        ],
        "RequestId": "d3d6f466-f2c2-44df-b78b-383ba717a3d8"
    }
}
```

