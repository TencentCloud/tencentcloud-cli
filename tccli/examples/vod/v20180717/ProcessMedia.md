**Example 1: 发起转码任务**

对 fileId 为 5285485487985271487 的视频发起转码任务，转出三种规格，使用的转码模板 ID 分别是20、30和40。

Input: 

```
tccli vod ProcessMedia --cli-unfold-argument  \
    --MediaProcessTask.TranscodeTaskSet.0.Definition 30 \
    --MediaProcessTask.TranscodeTaskSet.1.Definition 20 \
    --MediaProcessTask.TranscodeTaskSet.2.Definition 40 \
    --FileId 5285485487985271487
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

**Example 2: 发起带水印的转码任务**

对 fileId 为 5285485487985271487 的视频发起转码任务，转出三种规格，使用的转码模板 ID 分别是20、30和40；并且所有转码视频都打上水印，水印的模板 ID 为15780。

Input: 

```
tccli vod ProcessMedia --cli-unfold-argument  \
    --MediaProcessTask.TranscodeTaskSet.0.Definition 30 \
    --MediaProcessTask.TranscodeTaskSet.0.WatermarkSet.0.Definition 15780 \
    --MediaProcessTask.TranscodeTaskSet.1.Definition 20 \
    --MediaProcessTask.TranscodeTaskSet.1.WatermarkSet.0.Definition 15780 \
    --MediaProcessTask.TranscodeTaskSet.2.Definition 40 \
    --MediaProcessTask.TranscodeTaskSet.2.WatermarkSet.0.Definition 15780 \
    --FileId 5285485487985271487
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

**Example 3: 发起转码和采样截图任务**

对 fileId 为 5285485487985271487 的视频发起转码任务，转出三种规格，使用的转码模板 ID 分别是20、30和40；同时还对视频做采样截图，使用的采样截图的模板 ID 是10。

Input: 

```
tccli vod ProcessMedia --cli-unfold-argument  \
    --MediaProcessTask.TranscodeTaskSet.0.Definition 30 \
    --MediaProcessTask.TranscodeTaskSet.1.Definition 20 \
    --MediaProcessTask.TranscodeTaskSet.2.Definition 40 \
    --MediaProcessTask.SampleSnapshotTaskSet.0.Definition 10 \
    --FileId 5285485487985271487
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

**Example 4: 发起智能内容分析任务**

对 fileId 为 5285485487985271487 的视频发起内容分析任务 (包括智能分类、智能标签、智能封面)，使用的内容分析的模板 ID 是 10。

Input: 

```
tccli vod ProcessMedia --cli-unfold-argument  \
    --AiAnalysisTask.Definition 10 \
    --FileId 5285485487985271487
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TaskId": "125xxx65-procedurev2-bffb15f07586237bcecodb01fac7kdikk"
    }
}
```

**Example 5: 发起内容审核任务**

对 fileId 为 5285485487985271487 的视频发起内容审核任务（令人反感的信息、不安全的信息、不适宜的信息），使用的内容审核模板 ID 是 10。

Input: 

```
tccli vod ProcessMedia --cli-unfold-argument  \
    --AiContentReviewTask.Definition 10 \
    --FileId 5285485487985271487
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

**Example 6: 发起内容识别任务**

对 fileId 为 5285485487985271487 的视频发起内容识别任务 (包括人脸识别)，使用的内容识别的模板 ID 是 10。

Input: 

```
tccli vod ProcessMedia --cli-unfold-argument  \
    --AiRecognitionTask.Definition 10 \
    --FileId 5285485487985271487
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc70006fje1",
        "TaskId": "125xxx65-procedurev2-bffb15f07586237bcecodb01fac7kdabc"
    }
}
```

