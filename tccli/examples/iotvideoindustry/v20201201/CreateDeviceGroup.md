**Example 1: 创建设备**



Input: 

```
tccli iotvideoindustry CreateDeviceGroup --cli-unfold-argument  \
    --GroupName myGroup \
    --GroupDescribe this is my group \
    --ParentId group_root
```

Output: 
```
{
    "Response": {
        "GroupId": "group-1234abcd",
        "RequestId": "d3d6f466-f2c2-44df-b78b-383ba717a3d8",
        "Status": "OK"
    }
}
```

