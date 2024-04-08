**Example 1: 上传IVR音频文件**



Input: 

```
tccli ccc UploadIvrAudio --cli-unfold-argument  \
    --SdkAppId 0 \
    --AudioList.0.CustomFileName abc \
    --AudioList.0.AudioUrl http://xxxx.com/a.mp3
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

