**Example 1: 更新关联**

更新关联

Input: 

```
tccli wedata UpdateChatTableRelation --cli-unfold-argument  \
    --WorkspaceId afs \
    --RoomKey vx \
    --RelationKey AEWR \
    --LeftTableKey WE \
    --RightTableKey asdf \
    --LeftColumnKey sd \
    --RightColumnKey sdd \
    --RelationType dff
```

Output: 
```
{
    "Response": {
        "Data": {
            "Key": "AEWR"
        },
        "RequestId": "0192d283-2a34-4056-b7b7-a94acdc4d0d0"
    }
}
```

