**Example 1: 调用成功示例**

调用成功示例

Input: 

```
tccli vclm SubmitImageAnimateJob --cli-unfold-argument  \
    --ImageUrl https://console.cloud.tencent.com/cos/image.png \
    --TemplateId ke3 \
    --EnableAudio True \
    --EnableBodyJoins True \
    --EnableSegment True \
    --LogoAdd 1 \
    --LogoParam.LogoUrl https://console.cloud.tencent.com/cos/logo.png \
    --LogoParam.LogoRect.X -222 \
    --LogoParam.LogoRect.Y -54 \
    --LogoParam.LogoRect.Width 202 \
    --LogoParam.LogoRect.Height 34
```

Output: 
```
{
    "Response": {
        "JobId": "1194931538865782784",
        "RequestId": "4e6722ba-367b-454e-add0-681a5c50fe20"
    }
}
```

