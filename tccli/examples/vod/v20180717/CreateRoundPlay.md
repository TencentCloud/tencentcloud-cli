**Example 1: 创建轮播播单**

新建一个轮播播单，可以指定轮播列表。

Input: 

```
tccli vod CreateRoundPlay --cli-unfold-argument  \
    --StartTime 2022-06-01T00:00:00+08:00 \
    --RoundPlaylist.0.FileId 528xxx5487985271487 \
    --RoundPlaylist.0.AudioVideoType Transcode \
    --RoundPlaylist.0.Definition 100210
```

Output: 
```
{
    "Response": {
        "RoundPlayId": "bffb15f07530b57bc1aabb01fac74bca",
        "Url": "http://domain/round-play/bffb15f07530b57bc1aabb01fac74bca/playlist.m3u8",
        "RequestId": "6xxxxe3a-6b8e-4b4e-9256-fdc700064ef3"
    }
}
```

