**Example 1: Creating a task template that supports only video opening and ending credits recognition**

This example shows you how to create a custom video content recognition template to enable only a video opening and ending credits recognition task.

Input: 

```
tccli vod CreateAIRecognitionTemplate --cli-unfold-argument  \
    --Name 'Video opening and ending credits recognition task template'\
    --Comment 'Template 1'\
    --HeadTailConfigure.Switch ON
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

**Example 2: Creating a template that supports multiple video content recognition tasks**

This example shows you how to create a custom video content recognition template to enable a splitting task and a face recognition task. The default face library is used, and the face recognition filter score is 90.

Input: 

```
tccli vod CreateAIRecognitionTemplate --cli-unfold-argument  \
    --Name 'Intelligent recognition template'\
    --Comment 'Template 2'\
    --SegmentConfigure.Switch ON\
    --FaceConfigure.Switch ON\
    --FaceConfigure.FaceLibrary Default\
    --FaceConfigure.Score 90
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

**Example 3: Creating a template that supports multiple recognition tasks and specifies the frame capturing interval**

This example shows you how to create a custom video content recognition template to enable a splitting task and a face recognition task. The default and custom face libraries are used, the face recognition filter score is 90, and the frame capturing interval is 1.0 second.

Input: 

```
tccli vod CreateAIRecognitionTemplate --cli-unfold-argument  \
    --Name 'Intelligent recognition template'\
    --Comment 'Template 3'\
    --SegmentConfigure.Switch ON\
    --FaceConfigure.Switch ON\
    --FaceConfigure.FaceLibrary All\
    --ScreenshotInterval 1.0
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

