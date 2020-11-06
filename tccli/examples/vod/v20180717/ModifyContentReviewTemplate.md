**Example 1: Modifying content audit template, enabling porn detection in video image, and specifying filter tag and threshold scores**

This example shows you how to modify a custom AI-based content audit template where the filter tag is specified as sexy, and the threshold scores for violation and human audit are changed to 90 and 60, respectively, for the porn detection in video image task.

Input: 

```
tccli vod ModifyContentReviewTemplate --cli-unfold-argument  \
    --Definition 30 \
    --PornConfigure.ImgReviewInfo.Switch ON \
    --PornConfigure.ImgReviewInfo.LabelSet sexy \
    --PornConfigure.ImgReviewInfo.BlockConfidence 90 \
    --PornConfigure.ImgReviewInfo.ReviewConfidence 60
```

Output: 
```
{
    "Response": {
        "RequestId": "67ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

**Example 2: Modifying content audit template and enabling porn detection in video image**

This example shows you how to modify a custom AI-based content audit template with no filter tags specified. The threshold scores for violation and human audit are changed to the default values for the porn detection in video image task.

Input: 

```
tccli vod ModifyContentReviewTemplate --cli-unfold-argument  \
    --Definition 30 \
    --PornConfigure.ImgReviewInfo.Switch ON
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

**Example 3: Modifying content audit template, enabling porn detection in video image, and specifying threshold scores**

This example shows you how to modify a custom AI-based content audit template with no filter tags specified. The threshold scores for violation and human audit are changed to 90 and 60, respectively, for the porn detection in video image task.

Input: 

```
tccli vod ModifyContentReviewTemplate --cli-unfold-argument  \
    --Definition 30 \
    --PornConfigure.ImgReviewInfo.Switch ON \
    --PornConfigure.ImgReviewInfo.BlockConfidence 90 \
    --PornConfigure.ImgReviewInfo.ReviewConfidence 60
```

Output: 
```
{
    "Response": {
        "RequestId": "82ae8d8e-dce3-4151-9d4b-5594145223e1"
    }
}
```

