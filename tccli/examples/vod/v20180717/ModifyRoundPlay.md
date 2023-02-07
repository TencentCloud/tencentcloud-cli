**Example 1: 修改轮播播单**

修改轮播信息，可以修改轮播播单文件，播单名称、描述等。

Input: 

```
tccli vod ModifyRoundPlay --cli-unfold-argument  \
    --RoundPlayId bffb15f07530b57bc1aabb01fac74bca \
    --RoundPlaylist.0.FileId 528xxx5487985271487 \
    --RoundPlaylist.0.AudioVideoType Transcode \
    --RoundPlaylist.0.Definition 100210
```

Output: 
```
{
    "Response": {
        "RequestId": "6xxxxe3a-6b8e-4b4e-9256-fdc700064ef3"
    }
}
```

