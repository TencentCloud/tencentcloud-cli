**Example 1: Enabling one recognition task while disabling another one**

This example shows you how to modify a custom video content recognition template to disable a video opening and ending credits recognition task and enable a video splitting recognition task.

Input: 

```
tccli vod ModifyAIRecognitionTemplate --cli-unfold-argument  \
    --Definition 30 \
    --HeadTailConfigure.Switch OFF \
    --SegmentConfigure.Switch ON
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

**Example 2: Modifying the frame capturing interval of content recognition**

This example shows you how to modify a custom intelligent recognition template to change the frame capturing interval to 0.5 seconds.

Input: 

```
tccli vod ModifyAIRecognitionTemplate --cli-unfold-argument  \
    --Definition 30 \
    --ScreenshotInterval 0.5
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

**Example 3: Disabling video opening and ending credits recognition task**

This example shows you how to modify a custom video content recognition template to disable a video opening and ending credits recognition task.

Input: 

```
tccli vod ModifyAIRecognitionTemplate --cli-unfold-argument  \
    --Definition 30 \
    --HeadTailConfigure.Switch OFF
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

