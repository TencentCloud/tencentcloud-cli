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
        "LyricsUrl": "http://125xxx.myqcloud.com/ly.vtt",
        "PreludeInterval": 24000,
        "DefinitionInfoSet": [
            {
                "Definition": "audio/lo",
                "Bitrate": 64000,
                "Size": 3298220
            }
        ],
        "KTVMusicBaseInfo": {
            "ComposerSet": [
                "方文山"
            ],
            "SingerInfoSet": [
                {
                    "SingerId": "sid-88djjdd",
                    "Name": "周杰伦"
                }
            ],
            "MusicId": "mid-1287djxxjx",
            "SingerSet": [
                "周杰伦"
            ],
            "TagSet": [
                "华语",
                "流行"
            ],
            "Duration": 241,
            "LyricistSet": [
                "方文山"
            ],
            "Name": "七里香"
        },
        "ChorusClipSet": [
            {
                "EndTime": 48000,
                "StartTime": 24000
            }
        ],
        "MidiJsonUrl": "http://125xxx.myqcloud.com/midi.json",
        "PlayToken": "e1173xx993311ddx3h3gg3d9gjg4j",
        "RequestId": "1901xx-233xxx-221-xx"
    }
}
```

