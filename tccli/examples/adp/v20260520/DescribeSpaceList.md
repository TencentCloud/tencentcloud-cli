**Example 1: 获取空间列表**



Input: 

```
tccli adp DescribeSpaceList --cli-unfold-argument  \
    --Query 名称
```

Output: 
```
{
    "Response": {
        "RequestId": "303d27fd-40cf-4087-8a26-7b55ef382d86",
        "SpaceList": [
            {
                "Description": "",
                "Name": "默认工作空间",
                "PermissionIdList": [],
                "SpaceId": "default_space"
            },
            {
                "Description": "描述修改",
                "Name": "测试名称修改",
                "PermissionIdList": [
                    "adpSpace.DeleteSpace",
                    "adpSpace.ModifySpace"
                ],
                "SpaceId": "rsWOboao"
            }
        ],
        "TotalCount": "2"
    }
}
```

