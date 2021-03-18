**Example 1: 根据设备ID查询设备所在分组信息**



Input: 

```
tccli iotvideoindustry DescribeDeviceGroup --cli-unfold-argument  \
    --DeviceIds 99999999991320000001_99999999991320000001 99999999991320000002_99999999991320000002
```

Output: 
```
{
    "Response": {
        "DevGroups": [
            {
                "DeviceId": "99999999991320000001_99999999991320000001",
                "GroupId": "group_root",
                "GroupPath": "",
                "ParentId": "",
                "Error": ""
            },
            {
                "DeviceId": "99999999991320000002_99999999991320000002",
                "GroupId": "group_root",
                "GroupPath": "",
                "ParentId": "",
                "Error": ""
            }
        ],
        "RequestId": "d3d6f466-f2c2-44df-b78b-383ba717a3d8"
    }
}
```

