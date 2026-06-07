**Example 1: 创作音乐**



Input: 

```
tccli vod CreateAigcAudioTask --cli-unfold-argument  \
    --SubAppId 251441341 \
    --ModelName MiniMaxMusic \
    --ModelVersion 2.0 \
    --SceneType music \
    --Prompt 一首欢乐的歌 \
    --OutputConfig.StorageMode Temporary \
    --OutputConfig.OutputAudioFormat mp3 \
    --AdditionalParameters {"lyrics": "大海啊，全是水，骏马啊，四条腿,***************"}
```

Output: 
```
{
    "Response": {
        "TaskId": "251441341-AigcAudioTask-ed886585de73592fca966e81b6bc2d20t",
        "RequestId": "a9a9e323-d543-4bd3-b638-5853763e90c7"
    }
}
```

