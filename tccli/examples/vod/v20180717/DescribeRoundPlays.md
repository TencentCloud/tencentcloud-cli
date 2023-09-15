**Example 1: 获取轮播播单列表**

获取所有轮播播单的播单列表、名称、描述等详细信息。

Input: 

```
tccli vod DescribeRoundPlays --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "RequestId": "6xxxxe3a-6b8e-4b4e-9256-fdc700064ef3",
        "RoundPlaySet": [
            {
                "Name": "Demo",
                "RoundPlayId": "bffb15f07530b57bc1aabb01fac74bca",
                "StartTime": "2022-06-01T00:00:00+08:00",
                "Desc": "Demo",
                "Url": "http://123.vod-qcloud.com/rplay/v1/xxxx/playlist.m3u8",
                "Status": "Enabled",
                "PlayBackMode": "Loop",
                "RoundPlaylist": [
                    {
                        "AudioVideoType": "Transcode",
                        "Definition": 100,
                        "FileId": "528xxx5487985271487"
                    }
                ]
            }
        ]
    }
}
```

