**Example 1: 创建支持多项视频内容识别任务的模板**

创建一个自定义视频内容识别模板，同时开启人脸识别任务，人脸库使用默认库，人脸识别过滤分数为 90 分。

Input: 

```
tccli mps CreateAIRecognitionTemplate --cli-unfold-argument  \
    --Comment 模板2 \
    --FaceConfigure.Switch ON \
    --FaceConfigure.Score 90 \
    --FaceConfigure.FaceLibrary Default \
    --Name 智能识别模板
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

**Example 2: 创建支持多项识别任务的模板，同时指定截帧间隔**

创建一个自定义视频内容识别模板，同时开启人脸识别任务，人脸库使用默认库及用户自定义库，人脸识别过滤分数为 90 分。

Input: 

```
tccli mps CreateAIRecognitionTemplate --cli-unfold-argument  \
    --Comment 模板3 \
    --FaceConfigure.Switch ON \
    --FaceConfigure.FaceLibrary All \
    --Name 智能识别模板
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

