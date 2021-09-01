**Example 1: 根据分组ID查询分组**



Input: 

```
tccli iotvideoindustry DescribeGroupById --cli-unfold-argument  \
    --GroupId group-xxx
```

Output: 
```
{
    "Response": {
        "Group": {
            "GroupName": "myGroup",
            "ParentId": "group_root",
            "GroupId": "group-xxx",
            "GroupPath": "/group-xxx",
            "GroupDescribe": "this is xxx",
            "DeviceNum": 2,
            "SubGroupNum": 0,
            "CreateTime": 1608256825
        },
        "RequestId": "d3d6f466-f2c2-44df-b78b-383ba717a3d8"
    }
}
```

