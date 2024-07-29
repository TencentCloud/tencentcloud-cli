**Example 1: 调用成功-图片url地址**

调用成功

Input: 

```
tccli vclm SubmitPortraitSingJob --cli-unfold-argument  \
    --AudioUrl https://***/test.mp3 \
    --ImageUrl https://***/test.png
```

Output: 
```
{
    "Response": {
        "JobId": "1199964964965990400",
        "RequestId": "79655032-c347-4f05-af23-ae80f7ff47eb"
    }
}
```

**Example 2: 调用失败-音频时长超限**

音频时长超限

Input: 

```
tccli vclm SubmitPortraitSingJob --cli-unfold-argument  \
    --AudioUrl https://***/durationInvalid.m4a \
    --ImageUrl https://***/aj.jpg
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.InvalidAudioDuration",
            "Message": "音频时长超出限定范围。上传音频的时长要求：在1秒到60秒范围内"
        },
        "RequestId": "9d314f18-3670-4793-bf4b-619b43494ac7"
    }
}
```

**Example 3: 调用失败-图片分辨率超限**

图片分辨率超限

Input: 

```
tccli vclm SubmitPortraitSingJob --cli-unfold-argument  \
    --AudioUrl https://***/test.mp3 \
    --ImageUrl https://***/resolutionInvalid.jpg
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.InvalidImageResolution",
            "Message": "图片分辨率超出限定范围。上传图片的长边分辨率要求：在0到2560范围内"
        },
        "RequestId": "29498231-20eb-43d1-bb3b-cc9e07978699"
    }
}
```

**Example 4: 调用失败-图片宽高比超限**

图片宽高比超限

Input: 

```
tccli vclm SubmitPortraitSingJob --cli-unfold-argument  \
    --AudioUrl https://***/test.mp3 \
    --ImageUrl https://***/ratioInvalid.jpg
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.InvalidImageAspectRatio",
            "Message": "图片宽高比超出限定范围。上传图片的宽高比要求：在0.5到2.0范围内"
        },
        "RequestId": "3c9cb9bd-5b2a-4b18-a890-73f7712ca2ce"
    }
}
```

**Example 5: 调用失败-图片大小超限**

图片大小超限

Input: 

```
tccli vclm SubmitPortraitSingJob --cli-unfold-argument  \
    --AudioUrl https://***/test.mp3 \
    --ImageUrl https://***/storageInvalid.jpg
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.InvalidImageSize",
            "Message": "图片大小超出限定范围。上传图片的大小要求：在0MB到10MB范围内"
        },
        "RequestId": "cd17e6bb-afdb-4bed-8a15-55c461333104"
    }
}
```

