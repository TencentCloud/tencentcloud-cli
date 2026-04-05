**Example 1: 更新数据集信息**



Input: 

```
tccli wedata UpdateApplicationDataset --cli-unfold-argument  \
    --Key fb9e4d1f176889318086406b99645 \
    --WorkspaceId 17663856806379896 \
    --DashboardAccessKey 801469279624839168 \
    --DisplayName 无标题数据集test
```

Output: 
```
{
    "Response": {
        "Data": {
            "DatasetVersion": 4,
            "Key": "fb9e4d1f176889318086406b99645"
        },
        "RequestId": "9d437982-4060-44d2-9f94-9406fe2b155f"
    }
}
```

