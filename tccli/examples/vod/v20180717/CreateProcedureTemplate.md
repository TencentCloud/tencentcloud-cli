**Example 1: 创建一个发起转码任务的任务流模板**

创建一个名为“我的一个任务流”的任务流模板，任务流转码20，30，40三种格式。

Input: 

```
tccli vod CreateProcedureTemplate --cli-unfold-argument  \
    --Name 我的一个任务流\
    --MediaProcessTask.TranscodeTaskSet.0.Definition 20\
    --MediaProcessTask.TranscodeTaskSet.1.Definition 30\
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

**Example 2: 创建一个发起带水印的转码任务的任务流模板**

创建一个名为“我的一个任务流”的任务流模板，转出20，30，40三种格式，并且转出的每一个视频都打上一个水印，水印的模板 ID 为15780。

Input: 

```
tccli vod CreateProcedureTemplate --cli-unfold-argument  \
    --Name 我的一个任务流\
    --MediaProcessTask.TranscodeTaskSet.0.Definition 20\
    --MediaProcessTask.TranscodeTaskSet.0.Watermarks.0.Definition 15780\
    --MediaProcessTask.TranscodeTaskSet.1.Definition 30\
    --MediaProcessTask.TranscodeTaskSet.1.Watermarks.0.Definition 15780\
    --MediaProcessTask.TranscodeTaskSet.2.Definition 40\
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

**Example 3: 创建一个发起转码和采样截图任务的任务流模板**

创建一个名为“我的一个任务流”的任务流模板，转出20，30，40三种格式，同时还对视频做采样截图，使用的采样截图的模板 ID 是10。

Input: 

```
tccli vod CreateProcedureTemplate --cli-unfold-argument  \
    --Name 我的一个任务流\
    --MediaProcessTask.TranscodeTaskSet.0.Definition 20\
    --MediaProcessTask.TranscodeTaskSet.1.Definition 30\
    --MediaProcessTask.TranscodeTaskSet.2.Definition 40\
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

**Example 4: 创建一个发起智能内容审核任务的任务流模板**

创建一个名为“我的一个任务流”的任务流模板，发起智能审核任务 (包括鉴黄、鉴政、鉴恐)，使用的内容审核模板 ID 是 10。

Input: 

```
tccli vod CreateProcedureTemplate --cli-unfold-argument  \
    --Name 我的一个任务流\
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
