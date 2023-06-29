**Example 1: 批量获取曲目详情**

批量获取曲目详情

Input: 

```
tccli yinsuda BatchDescribeKTVMusicDetails --cli-unfold-argument  \
    --UserId userid1 \
    --MusicIds mid-47n6qwV1 testdddd \
    --AppName AppName1 \
    --PlayScene Live \
    --GuestUserId userid2 \
    --RoomId 1883
```

Output: 
```
{
    "Response": {
        "KTVMusicDetailInfoSet": [
            {
                "ChorusClipSet": [
                    {
                        "EndTime": 55206,
                        "StartTime": 37988
                    }
                ],
                "KTVMusicBaseInfo": {
                    "AlbumInfo": {
                        "CoverInfoSet": [
                            {
                                "Dimension": "Mini",
                                "Url": "http://imge.xxxx.com/stdmusic/150/20220521/20220521000237730193.jpg"
                            },
                            {
                                "Dimension": "Small",
                                "Url": "http://imge.xxxx.com/stdmusic/240/20220521/20220521000237730193.jpg"
                            },
                            {
                                "Dimension": "Medium",
                                "Url": "http://imge.xxxx.com/stdmusic/480/20220521/20220521000237730193.jpg"
                            }
                        ],
                        "Name": "予·君"
                    },
                    "Duration": 210051,
                    "MusicId": "mid-47n6qwV1",
                    "Name": "踏雪",
                    "RightSet": [
                        "Play",
                        "Sing"
                    ],
                    "SingerImageUrl": "http://singerimg.xxxx.com/uploadpic/softhead/150/20220329/20220329151558179.jpg",
                    "SingerSet": [
                        "等什么君(邓寓君)",
                        "FOX胡天渝"
                    ],
                    "RecommendType": "Other"
                },
                "LyricsUrl": "https://mcetest.ame.qcloud.com/download?sign=xxxxx&source=%2FLyrics%2F47n6qwV1%2Fsubtitle.vtt&t=1653897260&us=1300054767_test_1111",
                "MidiUrl": "https://mcetest.ame.qcloud.com/download?sign=xxxx&source=%2FPitch%2F47n6qwV1%2Fmusic.pitch&t=1653897260&us=1300054767_test_1111",
                "PlayToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJBcHBJZCI6MTMwMDA1NDc2NywiQXBwTmFtZSI6InRlc3QiLCJDdXJUaW1lIjowLCJFeHBpcmVUaW1lIjoxNjUzOTA0NDYwLCJNdXNpY0lkIjoibWlkLTQ3bjZxd1YxIiwiVXNlcklkIjoiMTExMSJ9.xxxxxiwlc",
                "GenreSet": [
                    "fg"
                ],
                "PreludeInterval": 12,
                "BPMInfo": {
                    "Type": "axx",
                    "Value": 12
                }
            }
        ],
        "NotExistMusicIdSet": [
            "testdddd"
        ],
        "RequestId": "8319127f-4284-4ac1-af40-8b195582256a"
    }
}
```

