**Example 1: 变更歌曲参数**

供TME侧进行变更歌曲参数

Input: 

```
tccli ame ModifyMusicOnShelves --cli-unfold-argument  \
    --MusicDetailInfos.HitWords xx \
    --MusicDetailInfos.Tags xx \
    --MusicDetailInfos.Bpm 0 \
    --MusicDetailInfos.AmeId xx \
    --MusicDetailInfos.MusicId xx \
    --MusicDetailInfos.Score 0.0
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

