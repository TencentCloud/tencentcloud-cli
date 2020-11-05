**Example 1: Creating a PowerPoint dynamic transcoding task**

This example shows how to create a dynamic transcoding task for a PowerPoint file and generate a 960×540 thumbnail.

Input: 

```
tccli tiw CreateTranscode --cli-unfold-argument  \
    --SdkAppId 1400000001\
    --Url https://path/to/document.ppt\
    --ThumbnailResolution 960x540
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

**Example 2: Creating a PowerPoint static transcoding task**

This example shows how to create a static transcoding task for a PowerPoint file.

Input: 

```
tccli tiw CreateTranscode --cli-unfold-argument  \
    --SdkAppId 1400000001\
    --Url https://path/to/document.ppt\
    --IsStaticPPT True
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

