**Example 1: 开始白板推流**



Input: 

```
tccli tiw StartWhiteboardPush --cli-unfold-argument  \
    --SdkAppId 1400000001 \
    --RoomId 1203 \
    --PushUserId tic_push_user_1203_141551 \
    --PushUserSig usersig_of_<tic_push_user_1203_141551>
```

Output: 
```
{
    "Response": {
        "Backup": "{\"RequestId\":\"8e9b2bc4-ec7f-46cd-823b-66676e2375f8\",\"TaskId\":\"052lfmu5uc3lp0rrqvvb\"}",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "TaskId": "bj0mt2l23osdj300hl30"
    }
}
```

