**Example 1: 点头/唇动检测**

点头使用场景：慧眼意愿核身产品目前使用语音方式确认用户意愿，但语音较容易受到各种因素的干扰(口音、语速、周边噪音等)，产品侧计划预研其它确认方式(如点头等)，用于提升用户体验及线上业务通过率。
说话使用场景：AI双录质检、意愿核身产品中需要进行用户语音确认，为避免语音是他人代答，需要加上张嘴说话动作的识别。


Input: 

```
tccli faceid FaceMotionDetection --cli-unfold-argument  \
    --VideoBase64 xxx \
    --VideoUrl xxxx \
    --ActionType 1
```

Output: 
```
{
    "Response": {
        "Result": "abc",
        "Description": "abc",
        "RequestId": "abc",
        "ActionFlag": true,
        "BestFrameBase64": "abc"
    }
}
```

