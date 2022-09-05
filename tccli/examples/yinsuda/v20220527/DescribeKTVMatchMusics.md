**Example 1: 匹配 AME 歌曲**



Input: 

```
tccli yinsuda DescribeKTVMatchMusics --cli-unfold-argument  \
    --Rules.0.AMEMusicId 1111003-xxx2-2edd \
    --UserId 10087 \
    --AppName test
```

Output: 
```
{
    "Response": {
        "NotMatchRuleSet": [],
        "MatchMusicSet": [
            {
                "MatchRule": {
                    "AMEMusicId": "1111003-xxx2-2edd"
                },
                "KTVMusicBaseInfo": {
                    "SingerImageUrl": "http://yinsuda.qcloud.com/1.jpg",
                    "Name": "一千年以后",
                    "MusicId": "mid-did2iixxx",
                    "RightSet": [
                        "Sing"
                    ],
                    "AlbumInfo": null,
                    "RecommendType": "Othter",
                    "SingerSet": [
                        "林俊杰"
                    ],
                    "Duration": 240000
                }
            }
        ],
        "RequestId": "58bfe77f-d477-48e8-9922-55f56d0b88fb"
    }
}
```

