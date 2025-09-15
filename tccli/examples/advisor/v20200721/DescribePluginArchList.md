**Example 1: 分页获取架构图列表**



Input: 

```
tccli advisor DescribePluginArchList --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 10 \
    --PluginKey xx
```

Output: 
```
{
    "Response": {
        "RequestId": "b90a5cc7-1a1e-4fcd-a7ee-46f767be7b38",
        "ArchList": [
            {
                "ArchId": "arch-xgosz3yz",
                "ArchName": "测试架构图1",
                "FolderId": 123,
                "CreateTime": "2023-11-14 15:22:32",
                "CreateUin": "123",
                "UpdateTime": "2023-11-14 15:22:32",
                "UpdateUin": "123",
                "ShareStatus": true,
                "ResourceBindStatus": true
            }
        ],
        "TotalCount": 1
    }
}
```

