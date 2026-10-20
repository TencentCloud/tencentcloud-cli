**Example 1: 视频深度估计示例（临时存储）**

对公网视频做深度估计，产物临时存储 7 天。

Input: 

```
tccli vod VideoDepthEstimation --cli-unfold-argument  \
    --SubAppId 1490012345 \
    --Url https://example.com/video.mp4
```

Output: 
```
{
    "Response": {
        "RequestId": "6d8e9a03-5c01-4a2b-8f3d-7e6c5b4a3d2e",
        "TaskId": "1490012345-VideoDepthEstimation-bffb15f07530b57bc1aabb01fac74bcat"
    }
}
```

**Example 2: 视频深度估计示例（永久存储）**

对已有媒资做深度估计，产物写入媒资库并指定名称与过期时间。

Input: 

```
tccli vod VideoDepthEstimation --cli-unfold-argument  \
    --SubAppId 1490012345 \
    --Url vod://5285890799710678156 \
    --OutputConfig.StorageMode Permanent \
    --OutputConfig.MediaName my-depth-video \
    --OutputConfig.ExpireTime 2026-12-31T00:00:00+08:00 \
    --SessionId SessionId \
    --SessionContext SessionContext \
    --TasksPriority 0
```

Output: 
```
{
    "Response": {
        "RequestId": "6d8e9a03-5c01-4a2b-8f3d-7e6c5b4a3d2e",
        "TaskId": "1490012345-VideoDepthEstimation-bffb15f07530b57bc1aabb01fac74bcat"
    }
}
```

