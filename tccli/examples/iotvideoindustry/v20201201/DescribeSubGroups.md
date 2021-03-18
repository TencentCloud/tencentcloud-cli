**Example 1: 查询子分组列表**



Input: 

```
tccli iotvideoindustry DescribeSubGroups --cli-unfold-argument  \
    --GroupId group_root
```

Output: 
```
{
    "Response": {
        "GroupList": [
            {
                "GroupName": "groupA",
                "ParentId": "group_root",
                "GroupId": "gro-30to7hxt",
                "GroupPath": "/gro-30to7hxt",
                "GroupDescribe": "this is xxx",
                "DeviceNum": 2,
                "SubGroupNum": 0,
                "CreateTime": 1608256825
            }
        ],
        "RequestId": "d3d6f466-f2c2-44df-b78b-383ba717a3d8",
        "TotalCount": 1
    }
}
```

