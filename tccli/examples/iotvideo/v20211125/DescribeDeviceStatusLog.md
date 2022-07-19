**Example 1: 获取设备上下线日志**



Input: 

```
tccli iotvideo DescribeDeviceStatusLog --cli-unfold-argument  \
    --MinTime 1548677099000 \
    --MaxTime 1548763499000 \
    --ProductId QY8BAN391G \
    --DeviceName dev_test \
    --Limit 5
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Listover": true,
        "Results": [
            {
                "Data": "xx",
                "Type": "xx",
                "Time": "xx"
            }
        ],
        "Context": "xx",
        "RequestId": "5e9bb8c5-95d3-40f8-ba9f-9d74a31004f2"
    }
}
```

