**Example 1: 批量查询分组信息**



Input: 

```
tccli iotvideoindustry DescribeGroups --cli-unfold-argument  \
    --GroupIds group-aaa group-bbb
```

Output: 
```
{
    "Response": {
        "Groups": [
            {
                "GroupId": "group-aaa",
                "GroupName": "分组A",
                "GroupPath": "/group-aaa",
                "ParentId": "group_root",
                "GroupDescribe": "this is xxx",
                "CreateTime": 1608256825,
                "ExtraInformation": "",
                "GroupStatus": 1,
                "Error": "",
                "GroupType": "NormalGroup"
            }
        ],
        "RequestId": "d3d6f466-f2c2-44df-b78b-383ba717a3d8"
    }
}
```

