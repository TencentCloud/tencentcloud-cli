**Example 1: Initiating an intelligent content analysis task**

This example shows you how to initiate a content analysis task (including intelligently generating category, tag, and cover) for the video with fileId of 5285485487985271487 by using content analysis template ID 10.

Input: 

```
tccli vod ProcessMedia --cli-unfold-argument  \
    --FileId 5285485487985271487\
    --AiAnalysisTask.Definition 10
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

**Example 2: Initiating a transcoding task**

This example shows you how to initiate a transcoding task for the video with the fileId of 5285485487985271487 to output in three specifications with transcoding template IDs 20, 30, and 40.

Input: 

```
tccli vod ProcessMedia --cli-unfold-argument  \
    --FileId 5285485487985271487\
    --MediaProcessTask.TranscodeTaskSet.0.Definition 20\
    --MediaProcessTask.TranscodeTaskSet.1.Definition 30\
    --MediaProcessTask.TranscodeTaskSet.2.Definition 40
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

**Example 3: Initiating an intelligent content recognition task**

This example shows you how to initiate a content recognition task (including face recognition) for the video with fileId of 5285485487985271487 by using content recognition template ID 10.

Input: 

```
tccli vod ProcessMedia --cli-unfold-argument  \
    --FileId 5285485487985271487\
    --AiRecognitionTask.Definition 10
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

**Example 4: Initiating a transcoding and sampled screencapturing task**

This example shows you how to initiate a transcoding task for the video with the fileId of 5285485487985271487 to output in three specifications with transcoding template IDs 20, 30, and 40, and screencapture the video with sampled screencapturing template ID 10.

Input: 

```
tccli vod ProcessMedia --cli-unfold-argument  \
    --FileId 5285485487985271487\
    --MediaProcessTask.TranscodeTaskSet.0.Definition 20\
    --MediaProcessTask.TranscodeTaskSet.1.Definition 30\
    --MediaProcessTask.TranscodeTaskSet.2.Definition 40\
    --MediaProcessTask.SampleSnapshotTaskSet.0.Definition 10
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

**Example 5: Initiating a transcoding task with watermark**

This example shows you how to initiate a transcoding task for the video with the fileId of 5285485487985271487 to output in three specifications with transcoding template IDs 20, 30, and 40. All the output videos are watermarked with the watermarking template ID 15780.

Input: 

```
tccli vod ProcessMedia --cli-unfold-argument  \
    --FileId 5285485487985271487\
    --MediaProcessTask.TranscodeTaskSet.0.Definition 20\
    --MediaProcessTask.TranscodeTaskSet.0.WatermarkSet.0.Definition 15780\
    --MediaProcessTask.TranscodeTaskSet.1.Definition 30\
    --MediaProcessTask.TranscodeTaskSet.1.WatermarkSet.0.Definition 15780\
    --MediaProcessTask.TranscodeTaskSet.2.Definition 40\
    --MediaProcessTask.TranscodeTaskSet.2.WatermarkSet.0.Definition 15780
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

**Example 6: Initiating an intelligent content audit task**

This example shows you how to initiate an intelligent content audit task (including detection of porn, politically sensitive, and terrorism information) for the video with fileId of 5285485487985271487 by using content audit template ID 10.

Input: 

```
tccli vod ProcessMedia --cli-unfold-argument  \
    --FileId 5285485487985271487\
    --AiContentReviewTask.Definition 10
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

