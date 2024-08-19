**Example 1: 插入一个节目到当前播放列表 a003 节目之后**



Input: 

```
tccli vod HandleCurrentPlaylist --cli-unfold-argument  \
    --SubAppId 123 \
    --RoundPlayId 130 \
    --Operation Insert \
    --ItemId a003 \
    --RoundPlaylist.0.FileId 528xxx5487985271487 \
    --RoundPlaylist.0.AudioVideoType Transcode \
    --RoundPlaylist.0.Definition 100210
```

Output: 
```
{
    "Response": {
        "RoundPlaylist": [
            {
                "ItemId": "a01",
                "AudioVideoType": "Transcode",
                "Definition": 100,
                "FileId": "528xxx5487985271487"
            }
        ],
        "RequestId": "6xxxxe3a-6b8e-4b4e-9256-fdc700064ef3"
    }
}
```

**Example 2: 删除播放列表中的节目**



Input: 

```
tccli vod HandleCurrentPlaylist --cli-unfold-argument  \
    --SubAppId 123 \
    --RoundPlayId 130 \
    --Operation Delete \
    --RoundPlaylist.0.ItemId a004 \
    --RoundPlaylist.0.FileId  \
    --RoundPlaylist.0.AudioVideoType 
```

Output: 
```
{
    "Response": {
        "RoundPlaylist": [
            {
                "ItemId": "a004",
                "AudioVideoType": "",
                "Definition": 100,
                "FileId": ""
            }
        ],
        "RequestId": "6xxxxe3a-6b8e-4b4e-9256-fdc700064ef3"
    }
}
```

