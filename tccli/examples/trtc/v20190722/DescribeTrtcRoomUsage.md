**Example 1: 查询TRTC音视频房间维度用量**

查询TRTC音视频房间维度用量

Input: 

```
tccli trtc DescribeTrtcRoomUsage --cli-unfold-argument  \
    --StartTime 2023-01-06 00:00 \
    --EndTime 2023-01-06 10:00 \
    --SdkAppid 1400017192
```

Output: 
```
{
    "Response": {
        "RequestId": "68fccf1c-c2c7-466a-9f14-1db4bed6054b",
        "Data": "RoomId,Audio,SD,hd,FullHD,2K,4K\ntest_room,1,2,3,4,5,6\n"
    }
}
```

