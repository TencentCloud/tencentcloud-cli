**Example 1: Creating a template that supports multiple video content recognition tasks**

This example shows you how to create a custom video content recognition template and enable a face recognition task. The default face library is used, and the face recognition filter score is 90.

Input: 

```
tccli mps CreateAIRecognitionTemplate --cli-unfold-argument  \
    --Name 'Intelligent recognition template'\
    --Comment 'Template 2'\
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

**Example 2: Creating a template that supports multiple recognition tasks and specifies the frame capturing interval**

This example shows you how to create a custom video content recognition template and enable a face recognition task. The default face library and custom library are used, and the face recognition filter score is 90.

Input: 

```
tccli mps CreateAIRecognitionTemplate --cli-unfold-argument  \
    --Name 'Intelligent recognition template'\
    --Comment 'Template 3'\
    --FaceConfigure.Switch ON\
    --FaceConfigure.FaceLibrary All
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

