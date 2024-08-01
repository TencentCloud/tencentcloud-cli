**Example 1: 查询黑白名单详情**



Input: 

```
tccli rce DescribeNameListDetail --cli-unfold-argument  \
    --BusinessSecurityData.NameListId 2446
```

Output: 
```
{
    "Response": {
        "Data": {
            "Code": 0,
            "Message": "OK",
            "Value": {
                "NameListId": 2446,
                "ListName": "测试",
                "ListType": 1,
                "DataType": 4,
                "SceneCode": "all_scene",
                "Status": 1,
                "Remark": "测试",
                "CreateTime": "2024-05-22 14:58:21",
                "UpdateTime": "2024-07-15 14:29:35",
                "EncryptionType": 0
            }
        },
        "RequestId": "bd2f3d71-9102-4c24-b581-4d4f22ebd077"
    }
}
```

