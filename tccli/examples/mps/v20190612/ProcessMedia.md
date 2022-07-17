**Example 1: 发起转码任务**

对指定 COS 地址的视频发起转码任务，转出20，30，40三种格式。

Input: 

```
tccli mps ProcessMedia --cli-unfold-argument  \
    --MediaProcessTask.TranscodeTaskSet.0.Definition 30 \
    --MediaProcessTask.TranscodeTaskSet.1.Definition 20 \
    --MediaProcessTask.TranscodeTaskSet.2.Definition 40 \
    --InputInfo.Type COS \
    --InputInfo.CosInputInfo.Region ap-chongqing \
    --InputInfo.CosInputInfo.Object /movie/201907/WildAnimal.mov \
    --InputInfo.CosInputInfo.Bucket TopRankVideo-125xxx88
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TaskId": "125xxx65-procedurev2-bffb15f07530b57bc1aabb01fac74bca"
    }
}
```

