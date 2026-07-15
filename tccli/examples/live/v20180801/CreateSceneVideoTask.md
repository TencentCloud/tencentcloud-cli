**Example 1: 请求示例**



Input: 

```
tccli live CreateSceneVideoTask --cli-unfold-argument  \
    --ModelName Kling \
    --ModelVersion 3.0 \
    --SceneType template_effect \
    --Prompt 生成一只小狗 \
    --Duration 5 \
    --ImageUrl https://m**********a*********344703.******cel******myqcloud.com/multimodel-agent-1258344703/***nt/ead65276-ba60-44b6-ac0d-81a4e1f****6.jpg \
    --LastImageUrl https://***ti*****-age**-1258****03.cos.***elerate.myqcloud.com/multimodel-agent-1258344703/agent*****5276-ba60-44b6-ac0d-81*****230b6.jpg \
    --ImageInfos.0.ImageUrl https://*****mod***agent-1258344703.***.a*****rate.myqcloud.com/multimo****agent-1258344703/agent/e*d65276-ba60-44b6-ac0d-81a4e1f***b6.jpg \
    --ImageInfos.0.Text 这是图1 \
    --ImageInfos.0.ReferenceType style \
    --VideoInfos.0.VideoUrl https://******u**ut-video-file-1326893053.cos.ap-gu***zhou.my**lo****om/4/4-AigcVideo-c77c36***16142******a44*6f134475_0.mp4 \
    --ExtraParameters.Resolution 1080P \
    --ExtraParameters.AspectRatio 16:9 \
    --ExtraParameters.OffPeak False \
    --ExtraParameters.LogoAdd True \
    --ExtraParameters.EnableAudio True \
    --ExtraParameters.EnableBgm True \
    --ExtraParameters.EnablePromptEnhance True \
    --AdditionalParameters {"effect_scene":"great_success"} \
    --StoreCosParam.CosBucketName live-****ud-tts-****402212 \
    --StoreCosParam.CosBucketRegion ap-guangzhou \
    --StoreCosParam.CosBucketPath /scene_video/ \
    --Operator admin
```

Output: 
```
{
    "Response": {
        "TaskId": "**10**278-live-*****ideo-721d18cefa094ba4a******dfcbbacab",
        "RequestId": "1f77ee4d-9802-40b5-aaa2-2752e8750590"
    }
}
```

