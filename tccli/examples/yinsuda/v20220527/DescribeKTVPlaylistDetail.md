**Example 1: 获取歌单详情**

获取歌单详情

Input: 

```
tccli yinsuda DescribeKTVPlaylistDetail --cli-unfold-argument  \
    --UserId 10087 \
    --PlaylistId pid-3dd22 \
    --Limit 10 \
    --AppName test
```

Output: 
```
{
    "Response": {
        "RequestId": "58bfe77f-d477-48e8-9922-55f56d0b88fb",
        "ScrollToken": "eyJDdXJQYWdlTnVtIjozLCJDdXJJbmRleCI6MH0=",
        "KTVMusicInfoSet": [
            {
                "AlbumInfo": {
                    "CoverInfoSet": [
                        {
                            "Dimension": "Mini",
                            "Url": "http://imge.xxxx.com/stdmusic/150/20191125/20191125163409414057.jpg"
                        },
                        {
                            "Dimension": "Small",
                            "Url": "http://imge.xxxx.com/stdmusic/240/20191125/20191125163409414057.jpg"
                        },
                        {
                            "Dimension": "Medium",
                            "Url": "http://imge.xxxx.com/stdmusic/480/20191125/20191125163409414057.jpg"
                        }
                    ],
                    "Name": "等"
                },
                "Duration": 216000,
                "MusicId": "mid-11x9dj3",
                "Name": "等",
                "RecommendType": "Other",
                "SingerImageUrl": "http://singerimg.xxxxx.com/uploadpic/softhead/150/20210326/20210326145830248137.jpg",
                "SingerSet": [
                    "贾振峰"
                ],
                "RightSet": [
                    "Play",
                    "Sing"
                ]
            }
        ]
    }
}
```

