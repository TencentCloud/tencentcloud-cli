**Example 1: Creating content audit template with only porn detection in video image enabled and specifying threshold scores and frame capturing interval**

This example shows you how to create a custom AI-based content audit template where porn detection in video image is enabled. The threshold scores for violation and human audit are set at 80 and 30, respectively.

Input: 

```
tccli mps CreateContentReviewTemplate --cli-unfold-argument  \
    --Name 'Content audit template'\
    --Comment 'Template 2'\
    --PornConfigure.ImgReviewInfo.Switch ON\
    --PornConfigure.ImgReviewInfo.BlockConfidence 80\
    --PornConfigure.ImgReviewInfo.ReviewConfidence 30
```

Output: 
```
{
    "Response": {
        "Definition": 31,
        "RequestId": "97aee3e9-2qd3-4151-9d4b-9730a45227a9"
    }
}
```

**Example 2: Creating content audit template with only porn detection in video image enabled**

This example shows you how to create a custom AI-based content audit template where only a porn detection in video image task is enabled. The default values are used as the threshold scores for violation and human audit, and filter tags are not specified.

Input: 

```
tccli mps CreateContentReviewTemplate --cli-unfold-argument  \
    --Name 'Content audit template'\
    --Comment 'Template 1'\
    --PornConfigure.ImgReviewInfo.Switch ON
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

**Example 3: Creating content audit template with multiple audit tasks enabled**

This example shows you how to create a custom AI-based content audit template where porn, terrorism, and politically sensitive information detection in video image tasks are enabled. The default values are used as the threshold scores for violation and human audit, and filter tags are not specified.

Input: 

```
tccli mps CreateContentReviewTemplate --cli-unfold-argument  \
    --Name 'Content audit template'\
    --Comment 'Template 3'\
    --PornConfigure.ImgReviewInfo.Switch ON\
    --TerrorismConfigure.ImgReviewInfo.Switch ON\
    --PoliticalConfigure.ImgReviewInfo.Switch ON
```

Output: 
```
{
    "Response": {
        "Definition": 32,
        "RequestId": "88aee3e9-2qd3-4151-9d4b-4390a45227a9"
    }
}
```

**Example 4: Creating content audit template with porn detection in video image enabled and specifying filter tags**

This example shows you how to create a custom AI-based content audit template where porn detection in video image is enabled. The filter tags are specified as porn and sexy, and the default values are used as the threshold scores for violation and human audit.

Input: 

```
tccli mps CreateContentReviewTemplate --cli-unfold-argument  \
    --Name 'Content audit template'\
    --Comment 'Template 1'\
    --PornConfigure.ImgReviewInfo.Switch ON\
    --PornConfigure.ImgReviewInfo.LabelSet porn sexy
```

Output: 
```
{
    "Response": {
        "Definition": 33,
        "RequestId": "67aee3e9-2qd3-2395-9d4b-4390a96837a7"
    }
}
```

