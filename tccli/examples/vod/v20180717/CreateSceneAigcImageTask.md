**Example 1: 发起生成场景化 AIGC 图片的任务**



Input: 

```
tccli vod CreateSceneAigcImageTask --cli-unfold-argument  \
    --SubAppId 251440382 \
    --SceneInfo.Type change_clothes \
    --SceneInfo.ChangeClothesConfig.ClothesFileInfos.0.FileId 3704211***509819 \
    --FileInfos.0.FileId 3704211***509820 \
    --OutputConfig.StorageMode Temporary \
    --OutputConfig.MediaName myfile \
    --OutputConfig.ClassId 0 \
    --SessionId mysession \
    --SessionContext mySessionContext \
    --TasksPriority 10 \
    --ExtInfo myextinfo
```

Output: 
```
{
    "Response": {
        "RequestId": "3185a050-c13a-4119-83a2-ed55802034c7",
        "TaskId": "251440382-SceneAigcImageTask-*****8a5d76bcacaaec9a6d823e4t"
    }
}
```

