**Example 1: 获取歌词信息**



Input: 

```
tccli ame DescribeLyric --cli-unfold-argument  \
    --ItemId xxxxx \
    --SubItemType LRC-LRC
```

Output: 
```
{
    "Response": {
        "Lyric": {
            "FileNameExt": "lrc",
            "SubItemType": "LRC-LRC",
            "Url": "http://xxx.com/lyric/09/860/9860965-LRC-LRC.lrc"
        },
        "RequestId": "s1568793079544475000"
    }
}
```

