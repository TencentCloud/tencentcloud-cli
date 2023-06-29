**Example 1: 申请合唱**

申请合唱相关信息

Input: 

```
tccli yinsuda ApplyChorus --cli-unfold-argument  \
    --UserId 20220123abc \
    --AppName test \
    --RoomId 100832 \
    --MusicId mid-112ddff \
    --ChorusUserIds user1 user2 \
    --MaxChorusNum 10
```

Output: 
```
{
    "Response": {
        "ChorusToken": "chid-9hh33x",
        "RequestId": "58bfe77f-d477-48e8-9922-55f56d0b88fb"
    }
}
```

