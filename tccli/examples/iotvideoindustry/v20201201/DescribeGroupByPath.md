**Example 1: 删除分组**



Input: 

```
tccli iotvideoindustry DescribeGroupByPath --cli-unfold-argument  \
    --GroupPath /group-aaa/group-bbb
```

Output: 
```
{
    "Response": {
        "Group": {
            "GroupName": "groupXXX",
            "ParentId": "group-aaa",
            "GroupId": "group-bbb",
            "GroupPath": "/group-aaa/group-bbb",
            "GroupDescribe": "this is xxx",
            "DeviceNum": 2,
            "SubGroupNum": 0,
            "CreateTime": 1608256825
        },
        "RequestId": "d3d6f466-f2c2-44df-b78b-383ba717a3d8"
    }
}
```

