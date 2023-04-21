**Example 1: 上传图片**

上传图片

Input: 

```
tccli trtc CreatePicture --cli-unfold-argument  \
    --Content test \
    --Suffix jpg \
    --SdkAppId 123 \
    --Height 12 \
    --Width 15 \
    --XPosition 15 \
    --YPosition 36
```

Output: 
```
{
    "Response": {
        "PictureId": 1400297109,
        "RequestId": "049461e6-f2f5-4168-887e-aca4fbfa5fae"
    }
}
```

