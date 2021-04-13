**Example 1: 创建设备**



Input: 

```
tccli iotvideoindustry CreateDevice --cli-unfold-argument  \
    --NickName myDevice \
    --PassWord password \
    --GroupId group_root
```

Output: 
```
{
    "Response": {
        "DeviceCode": "99999999991320000001",
        "DeviceId": "99999999991320000001_99999999991320000001",
        "VirtualGroupId": "",
        "RequestId": "d3d6f466-f2c2-44df-b78b-383ba717a3d8"
    }
}
```

