**Example 1: 查询轮播当前播放列表。**



Input: 

```
tccli vod DescribeCurrentPlaylist --cli-unfold-argument  \
    --RoundPlayId 1323 \
    --SubAppId 123
```

Output: 
```
{
    "Response": {
        "CurrentPlaylist": [
            {
                "ItemId": "a001",
                "FileId": "528xxx5487985271487",
                "StartPlayTime": "2024-07-25T10:12:00+08:00",
                "Duration": 100
            }
        ],
        "RequestId": "58759c60-aceb-4b02-b0ed-6c62bfea88cc"
    }
}
```

