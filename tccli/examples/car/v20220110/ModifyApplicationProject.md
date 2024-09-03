**Example 1: 修改云应用项目请求**

用于修改云应用项目

Input: 

```
tccli car ModifyApplicationProject --cli-unfold-argument  \
    --IsPreload True \
    --ProjectId abc \
    --ApplicationParams abc \
    --Name abc \
    --Type L1 \
    --FPS 0 \
    --PreloadDuration 10s \
    --ReconnectTimeout 20s \
    --MinBitrate 0 \
    --MaxBitrate 10 \
    --DisableVideoCodecs H265
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

