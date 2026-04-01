**Example 1: 分页查询标签**



Input: 

```
tccli wedata ListLabels --cli-unfold-argument  \
    --WorkspaceId 1 \
    --Page.PageSize 1 \
    --Page.PageNumber 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "Labels": [],
            "Message": "查询成功",
            "TotalCount": "1"
        },
        "RequestId": "8888c83e-a561-4723-85c4-35a884c12e9b"
    }
}
```

