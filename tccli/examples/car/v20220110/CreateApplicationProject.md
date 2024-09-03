**Example 1: 创建云应用项目示例**

用于创建云应用项目

Input: 

```
tccli car CreateApplicationProject --cli-unfold-argument  \
    --Name abc \
    --ApplicationId abc \
    --Type abc \
    --IsPreload True \
    --ApplicationParams abc \
    --Resolution abc \
    --ProjectType abc \
    --FPS 0 \
    --PreloadDuration 10s \
    --ReconnectTimeout 20s \
    --MinBitrate 0 \
    --MaxBitrate 10
```

Output: 
```
{
    "Response": {
        "ProjectId": "abc",
        "RequestId": "abc"
    }
}
```

