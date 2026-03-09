**Example 1: 查询信令录制回放观看记录。**



Input: 

```
tccli lcic DescribePlayRecords --cli-unfold-argument  \
    --SdkAppId 3520371 \
    --RoomId 322220255 \
    --StartTime 1770174290 \
    --EndTime 1770260690 \
    --Page 1 \
    --PageSize 10 \
    --UserId 2qkMhWixIzNQC7UizlM7*******
```

Output: 
```
{
    "Response": {
        "Records": [
            {
                "Duration": 93677,
                "PlayBeginTime": 1770184233,
                "PlayEndTime": 1770184329,
                "RoomId": 322220255,
                "SessionId": "322220255-1770184231997-1345",
                "UserId": "2qkMhWixIzNQC7UizlM7*******"
            }
        ],
        "Total": 8,
        "RequestId": "c29649d6-a8c7-4c0c-923f-ad569af81598"
    }
}
```

