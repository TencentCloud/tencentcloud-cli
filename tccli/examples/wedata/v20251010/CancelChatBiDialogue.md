**Example 1: 取消对话**



Input: 

```
tccli wedata CancelChatBiDialogue --cli-unfold-argument  \
    --Key 48eb050f17701245381251a0172cd \
    --TaskKey f2e373ae1770124538118f8664664 \
    --ConnectionId connectionId_93d740b0_f39c21ef-bfdf-4cb0-9627-9a07d92ab4e0 \
    --WorkspaceId 17678671667189298 \
    --RoomKey 803627528827023360
```

Output: 
```
{
    "Response": {
        "Data": {
            "Key": "48eb050f17701245381251a0172cd",
            "TaskKey": "f2e373ae1770124538118f8664664",
            "ConnectionId": "connectionId_93d740b0_f39c21ef-bfdf-4cb0-9627-9a07d92ab4e0",
            "WorkspaceId": "17678671667189298",
            "RoomKey": "803627528827023360",
            "Message": "取消成功",
            "Success": true
        },
        "RequestId": "1bf35a2d-c760-4f97-9b2b-e327bcd62a43"
    }
}
```

