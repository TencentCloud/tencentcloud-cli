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
        "RequestId": "7b9d6abb-4ec1-4ef3-b904-2b11e24012f3"
    }
}
```

**Example 2: 修改播单过期时间为2024-12-10T23:00:00+08:00**

修改 bffb15f07530b57bc1aabb01fac74bca 播单的过期时间为2024-12-10T23:00:00+08:00

Input: 

```
tccli vod ModifyRoundPlay --cli-unfold-argument  \
    --RoundPlayId bffb15f07530b57bc1aabb01fac74bca \
    --ExpiredTime 2024-12-10T23:00:00+08:00
```

Output: 
```
{
    "Response": {
        "RequestId": "7b9d6abb-4ec1-4ef3-b904-2b11e24012f5"
    }
}
```

