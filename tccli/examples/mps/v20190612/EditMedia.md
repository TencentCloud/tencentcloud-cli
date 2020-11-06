**Example 1: 对一个文件进行剪辑，生成一个新的视频**



Input: 

```
tccli mps EditMedia --cli-unfold-argument  \
    --FileInfos.0.InputInfo.Type COS \
    --FileInfos.0.InputInfo.CosInputInfo.Bucket TopRankVideo-125xxx88 \
    --FileInfos.0.InputInfo.CosInputInfo.Region ap-chongqing \
    --FileInfos.0.InputInfo.CosInputInfo.Object /movie/201907/WildAnimal.mov \
    --FileInfos.0.StartTimeOffset 60.0 \
    --FileInfos.0.EndTimeOffset 120.0 \
    --OutputStorage.Type COS \
    --OutputStorage.CosOutputStorage.Bucket TopRankVideo-125xxx88 \
    --OutputStorage.CosOutputStorage.Region ap-chongqing \
    --OutputObjectPath /clip_result/clip_WildAnimal.{format}
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TaskId": "125xxx88-EditMedia-bffb15f07530b57bc1aabb01fac74bca"
    }
}
```

