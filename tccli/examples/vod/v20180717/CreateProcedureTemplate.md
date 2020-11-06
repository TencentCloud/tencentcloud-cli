**Example 1: Creating a task flow template that initiates a transcoding and sampled screencapturing task**

This example shows you how to create a task flow template named "My Task Flow" to transcode a video into three formats of 20, 30, and 40 and screencapture the video with sampled screencapturing template ID 10.

Input: 

```
tccli vod CreateProcedureTemplate --cli-unfold-argument  \
    --Name 'My Task Flow' \
    --MediaProcessTask.TranscodeTaskSet.0.Definition 20 \
    --MediaProcessTask.TranscodeTaskSet.1.Definition 30 \
    --MediaProcessTask.TranscodeTaskSet.2.Definition 40 \
    --MediaProcessTask.SampleSnapshotTaskSet.0.Definition 10
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3"
    }
}
```

**Example 2: Creating a task flow template that initiates a transcoding task**

This example shows you how to create a task flow template named "My Task Flow" to transcode a video into three formats of 20, 30, and 40.

Input: 

```
tccli vod CreateProcedureTemplate --cli-unfold-argument  \
    --Name 'My Task Flow' \
    --MediaProcessTask.TranscodeTaskSet.0.Definition 20 \
    --MediaProcessTask.TranscodeTaskSet.1.Definition 30 \
    --MediaProcessTask.TranscodeTaskSet.2.Definition 40
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3"
    }
}
```

**Example 3: Creating a task flow template that initiates an intelligent content audit task**

This example shows you how to create a task flow template named "My Task Flow" to initiate an intelligent content audit task (including detection of porn, politically sensitive, and terrorism information) with content audit template ID 10.

Input: 

```
tccli vod CreateProcedureTemplate --cli-unfold-argument  \
    --Name 'My Task Flow' \
    --AiContentReviewTask.Definition 10
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3"
    }
}
```

**Example 4: Creating a task flow template that initiates a transcoding task with watermark**

This example shows you how to create a task flow template named "My Task Flow" to transcode a video into three formats of 20, 30, and 40, where each output video has a watermark added by watermarking template ID 15780.

Input: 

```
tccli vod CreateProcedureTemplate --cli-unfold-argument  \
    --Name 'My Task Flow' \
    --MediaProcessTask.TranscodeTaskSet.0.Definition 20 \
    --MediaProcessTask.TranscodeTaskSet.0.Watermarks.0.Definition 15780 \
    --MediaProcessTask.TranscodeTaskSet.1.Definition 30 \
    --MediaProcessTask.TranscodeTaskSet.1.Watermarks.0.Definition 15780 \
    --MediaProcessTask.TranscodeTaskSet.2.Definition 40 \
    --MediaProcessTask.TranscodeTaskSet.2.Watermarks.0.Definition 15780
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3"
    }
}
```

