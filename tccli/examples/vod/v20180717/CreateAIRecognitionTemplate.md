**Example 1: 创建仅支持视频片头片尾识别的任务模板**

创建一个自定义音视频内容识别模板，仅开启视频片头片尾识别任务。

Input: 

```
tccli vod CreateAIRecognitionTemplate --cli-unfold-argument  \
    --Comment 模板1 \
    --HeadTailConfigure.Switch ON \
    --Name 视频片头片尾识别任务模板
```

Output: 
```
{
    "Response": {
        "Definition": 30,
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

**Example 2: 创建仅支持语音翻译的任务模板**

创建一个自定义音视频内容识别模板，仅开启语音翻译任务。

Input: 

```
tccli vod CreateAIRecognitionTemplate --cli-unfold-argument  \
    --AsrTranslateConfigure.Switch ON \
    --AsrTranslateConfigure.SrcLanguage zh \
    --AsrTranslateConfigure.DstLanguage en \
    --AsrTranslateConfigure.SubtitleFormats vtt \
    --Name 语音翻译模板_中译英
```

Output: 
```
{
    "Response": {
        "Definition": 31,
        "RequestId": "0de23d47-ff58-41d7-80c4-c4fa7dbc6c21"
    }
}
```

**Example 3: 创建支持多项识别任务的模板，同时指定截帧间隔**

创建一个自定义音视频内容识别模板，开启拆条任务，同时开启人脸识别任务，人脸库使用默认库及用户自定义库，人脸识别过滤分数为 90 分，指定截帧间隔为 1.0  秒。

Input: 

```
tccli vod CreateAIRecognitionTemplate --cli-unfold-argument  \
    --Comment 模板3 \
    --FaceConfigure.Switch ON \
    --FaceConfigure.FaceLibrary All \
    --ScreenshotInterval 1.0 \
    --Name 智能识别模板 \
    --SegmentConfigure.Switch ON
```

Output: 
```
{
    "Response": {
        "Definition": 32,
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

**Example 4: 创建支持多项音视频内容识别任务的模板**

创建一个自定义音视频内容识别模板，开启拆条任务，同时开启人脸识别任务，人脸库使用默认库，人脸识别过滤分数为 90 分。

Input: 

```
tccli vod CreateAIRecognitionTemplate --cli-unfold-argument  \
    --Comment 模板2 \
    --FaceConfigure.Switch ON \
    --FaceConfigure.Score 90 \
    --FaceConfigure.FaceLibrary Default \
    --Name 智能识别模板 \
    --SegmentConfigure.Switch ON
```

Output: 
```
{
    "Response": {
        "Definition": 31,
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

