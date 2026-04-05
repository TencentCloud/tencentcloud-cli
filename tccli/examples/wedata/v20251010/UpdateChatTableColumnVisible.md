**Example 1: 更新字段可见/不可见**

更新字段可见/不可见

Input: 

```
tccli wedata UpdateChatTableColumnVisible --cli-unfold-argument  \
    --WorkspaceId asd \
    --RoomKey asd \
    --TableKey asd \
    --ColumnKeyList asd \
    --VisibleStatus 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "ColumnKeyList": []
        },
        "RequestId": "a45499bb-43ad-4711-8023-9f085a159ed1"
    }
}
```

