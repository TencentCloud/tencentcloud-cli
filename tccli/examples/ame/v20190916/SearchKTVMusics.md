**Example 1: 搜索 KTV 歌曲**



Input: 

```
tccli ame SearchKTVMusics --cli-unfold-argument  \
    --Limit 10 \
    --KeyWord 周杰伦 \
    --Offset 0
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
                "MusicId": "ame-78dxxx",
                "SingerSet": [
                    "周杰伦"
                ],
                "Name": "七里香",
                "LyricistSet": [
                    "周杰伦"
                ],
                "TagSet": [
                    "华语",
                    "流行"
                ]
            }
        ],
        "RequestId": "xx"
    }
}
```

