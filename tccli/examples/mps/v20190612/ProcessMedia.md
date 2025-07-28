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

**Example 2: 发起媒体质检任务**



Input: 

```
tccli mps ProcessMedia --cli-unfold-argument  \
    --InputInfo.Type COS \
    --InputInfo.CosInputInfo.Bucket TopRankVideo-125xxx88 \
    --InputInfo.CosInputInfo.Region ap-shanghai \
    --InputInfo.CosInputInfo.Object /image/lenna.jpeg \
    --OutputStorage.Type COS \
    --OutputStorage.CosOutputStorage.Bucket TopRankVideo-125xxx88 \
    --OutputStorage.CosOutputStorage.Region ap-shanghai \
    --OutputDir /data/share/ \
    --AiQualityControlTask.Definition 30
```

Output: 
```
{
    "Response": {
        "RequestId": "4a72e698-ec27-4fc1-8e17-c1cbfce1a4a9",
        "TaskId": "2600007696-WorkflowTask-67771a50b24d08baaf6165da23461e36tt7"
    }
}
```

**Example 3: 发起自适应码流任务**



Input: 

```
tccli mps ProcessMedia --cli-unfold-argument  \
    --InputInfo.Type COS \
    --InputInfo.CosInputInfo.Bucket TopRankVideo-125xxx88 \
    --InputInfo.CosInputInfo.Region ap-shanghai \
    --InputInfo.CosInputInfo.Object /video/lego-city-vehicles.mp4 \
    --OutputDir /share/output/ \
    --MediaProcessTask.AdaptiveDynamicStreamingTaskSet.0.Definition 10 \
    --MediaProcessTask.AdaptiveDynamicStreamingTaskSet.0.OutputObjectPath {inputName}_adaptiveDynamicStreaming.{format} \
    --MediaProcessTask.AdaptiveDynamicStreamingTaskSet.0.SubStreamObjectName {inputName}_adaptiveDynamicStreaming_{definition}_{subStreamNumber}.{format} \
    --MediaProcessTask.AdaptiveDynamicStreamingTaskSet.0.SegmentObjectName {inputName}_adaptiveDynamicStreaming_{definition}_{subStreamNumber}_{segmentNumber}.{format}
```

Output: 
```
{
    "Response": {
        "RequestId": "be6954ba-1e0e-4b36-9da1-d79aaaaccb0d",
        "TaskId": "2600007696-WorkflowTask-7bc4b70f5bda4b4fef4ad29d2d168bdftt7"
    }
}
```

