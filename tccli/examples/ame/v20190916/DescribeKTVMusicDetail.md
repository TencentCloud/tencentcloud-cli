**Example 1: 查询 KTV 曲目详情**



Input: 

```
tccli ame DescribeKTVMusicDetail --cli-unfold-argument  \
    --MusicId ame-78d2xxx
```

Output: 
```
{
    "Response": {
        "LyricsUrl": "xx",
        "PreludeInterval": 0,
        "DefinitionInfoSet": [
            {
                "Definition": "xx",
                "Bitrate": 64000,
                "Size": 3298220
            }
        ],
        "KTVMusicBaseInfo": {
            "ComposerSet": [
                "周杰伦"
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
                "方文山"
            ],
            "Name": "xx"
        },
        "ChorusClipSet": [
            {
                "EndTime": 0,
                "StartTime": 0
            }
        ],
        "MidiJsonUrl": "xx",
        "PlayToken": "xx",
        "RequestId": "xx"
    }
}
```

