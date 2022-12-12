**Example 1: 创建PPT动态转码任务**

创建PPT动态转码任务，并生成分辨率为960x540的缩略图

Input: 

```
tccli tiw CreateTranscode --cli-unfold-argument  \
    --Url https://path/to/document.ppt \
    --ThumbnailResolution 960x540 \
    --SdkAppId 1400000001
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "TaskId": "g6ls63ps49vteb8bk1mb"
    }
}
```

**Example 2: 创建PPT静态转码任务**

创建PPT静态转码任务

Input: 

```
tccli tiw CreateTranscode --cli-unfold-argument  \
    --Url https://path/to/document.ppt \
    --IsStaticPPT True \
    --SdkAppId 1400000001
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "TaskId": "g6ls63ps49vteb8bk1mb"
    }
}
```

