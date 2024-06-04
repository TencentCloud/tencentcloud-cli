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
        "MatchMusicSet": [
            {
                "KTVMusicBaseInfo": {
                    "MusicId": "3mcwprujq9",
                    "Name": "七里香",
                    "SingerSet": [
                        "周杰伦"
                    ],
                    "Duration": 120,
                    "SingerImageUrl": "http://image.tencent.com",
                    "AlbumInfo": {
                        "Name": "一个浪漫的专辑",
                        "CoverInfoSet": [
                            {
                                "Dimension": "Mini",
                                "Url": "http://download.tencent.com"
                            }
                        ]
                    },
                    "RightSet": [
                        "Play"
                    ],
                    "RecommendType": "Featured"
                },
                "MatchRule": {
                    "AMEMusicId": "bmp7a8yut5",
                    "MusicInfo": {
                        "MusicName": "反方向的钟",
                        "SingerSet": [
                            "周杰伦",
                            "陈奕迅"
                        ]
                    },
                    "MusicIdToMatchAME": "hr9nqvkz46"
                },
                "AMEMusicBaseInfo": {
                    "MusicId": "bmp7a8yut5",
                    "Name": "反方向的钟",
                    "SingerSet": [
                        "周杰伦",
                        "陈奕迅"
                    ]
                }
            }
        ],
        "NotMatchRuleSet": [
            {
                "AMEMusicId": "abc",
                "MusicInfo": {
                    "MusicName": "abc",
                    "SingerSet": [
                        "abc"
                    ]
                },
                "MusicIdToMatchAME": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

