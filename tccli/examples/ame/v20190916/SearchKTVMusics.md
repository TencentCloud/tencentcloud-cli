**Example 1: 搜索 KTV 歌曲**



Input: 

```
tccli ame SearchKTVMusics --cli-unfold-argument  \
    --Limit 10 \
    --KeyWord 周杰伦 \
    --Sort.Field xx \
    --Sort.Order xx \
    --Offset 0 \
    --TagIds xx
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "KTVMusicInfoSet": [
            {
                "ComposerSet": [
                    "方文山"
                ],
                "SingerInfoSet": [
                    {
                        "SingerId": "xx",
                        "Name": "xx"
                    }
                ],
                "MusicId": "xx",
                "SingerSet": [
                    "周杰伦"
                ],
                "TagSet": [
                    "华语",
                    "流行"
                ],
                "Duration": 1,
                "LyricistSet": [
                    "周杰伦"
                ],
                "Name": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

