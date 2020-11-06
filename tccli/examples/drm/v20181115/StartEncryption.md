**Example 1: 请求示例**

演示启动一次fairplay方案的加密

Input: 

```
tccli drm StartEncryption --cli-unfold-argument  \
    --CosEndPoint cos.ap-hongkong.myqcloud.com \
    --CosSecretId 'your secretID' \
    --CosSecretKey 'your secret key' \
    --DrmType FAIRPLAY \
    --SourceObject.BucketName drm-unencrypt-1234567 \
    --SourceObject.ObjectName in.mp4 \
    --OutputObjects.0.BucketName drm-encrypt-1234567 \
    --OutputObjects.0.ObjectName out.m3u8 \
    --OutputObjects.0.Para.Type m3u8 \
    --OutputObjects.1.BucketName drm-encrypt-1234567 \
    --OutputObjects.1.ObjectName out.ts \
    --OutputObjects.1.Para.Type audio
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

