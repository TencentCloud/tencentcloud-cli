**Example 1: 请求示例**



Input: 

```
tccli mps CreateAigcAudioTask --cli-unfold-argument  \
    --ModelName Tme \
    --ModelVersion 1.0 \
    --SceneType music \
    --Prompt 生成一段音乐 \
    --VideoInfos.0.VideoUrl https://l***-******-tts-131140***2.c***ap-*ua****ou.myqcloud.com/251006278_1513228070381297256.mp4 \
    --AudioInfos.0.AudioUrl https://li**-q*******ts-1311402212*cos*ap-guangzh****yqcloud.com/25*******_1513228070381297256.wav \
    --OutputAudioFormat wav \
    --ExtraParameters.ResourceId 438910555_1 \
    --AdditionalParameters {"sequential_image_generation":"auto"} \
    --Operator admin
```

Output: 
```
{
    "Response": {
        "TaskId": "24*******AigcAudio-6a38**3a9f51468da5bfc25****9a462",
        "RequestId": "fcc72969-6464-45ba-8369-232f7a1e1c76"
    }
}
```

