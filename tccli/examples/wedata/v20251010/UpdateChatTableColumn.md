**Example 1: 更新chat数据表**

更新chat数据表

Input: 

```
tccli wedata UpdateChatTableColumn --cli-unfold-argument  \
    --WorkspaceId sdaf \
    --RoomKey as \
    --TableKey sd \
    --ColumnKey fd \
    --ColumnName sds \
    --UserComment sdff \
    --VisibleStatus 1 \
    --SynonymList s
```

Output: 
```
{
    "Response": {
        "Data": {
            "ColumnKey": "234234"
        },
        "RequestId": "050f9676-199b-4f20-83b2-df8549db78a5"
    }
}
```

