**Example 1: 获取直播互动曲库歌曲的周榜和月榜**

获取直播互动曲库歌曲的周榜和月榜

Input: 

```
tccli ame DescribeKTVTopList --cli-unfold-argument  \
    --Type Hot \
    --Period Week
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "1999xff-11122",
        "KTVMusicTopInfoSet": [
            {
                "ComposerSet": [
                    "方文山"
                ],
                "SingerInfoSet": [
                    {
                        "SingerId": "amesid-98dssf",
                        "Name": "周杰伦"
                    }
                ],
                "MusicId": "ameid-34dd8d9s",
                "TagSet": [
                    "情歌"
                ],
                "Duration": 240,
                "LyricistSet": [
                    "方文山"
                ],
                "Name": "七里香"
            }
        ]
    }
}
```

