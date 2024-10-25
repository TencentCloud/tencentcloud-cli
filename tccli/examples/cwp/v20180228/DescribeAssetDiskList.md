**Example 1: 获取主机磁盘列表**



Input: 

```
tccli cwp DescribeAssetDiskList --cli-unfold-argument  \
    --Quuid 6cf3c132-aaaa-bbbb-b08d-98be9421372a \
    --Uuid 6cf3c132-aaaa-bbbb-b08d-98be9421372a \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Disks": [
            {
                "Name": "disk1",
                "Size": 1024000,
                "Percent": 50,
                "Type": "ext4",
                "Path": "/data",
                "Used": 10
            }
        ],
        "Total": 1,
        "RequestId": "07a92740-5e54-4ea6-9320-c6fc3f3a1121"
    }
}
```

