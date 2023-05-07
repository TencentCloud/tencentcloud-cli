**Example 1: 调用成功示例**

查询当前用户的图片库信息。

Input: 

```
tccli tiia DescribeGroups --cli-unfold-argument  \
    --Offset 0 \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "Groups": [
            {
                "Brief": "",
                "CreateTime": "2023-02-02 18:04:08",
                "GroupId": "group_test_id",
                "GroupName": "group_test_id_name",
                "GroupType": 4,
                "MaxCapacity": 10000,
                "MaxQps": 10,
                "PicCount": 1,
                "UpdateTime": "2023-02-02 18:04:41"
            }
        ],
        "RequestId": "347a9402-b68c-42d0-8a75-d1b123fe83d5"
    }
}
```

