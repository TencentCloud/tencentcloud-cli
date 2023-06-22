**Example 1: 发起音画质检测任务**

对 fileId 为 5285485487985271487 的视频发起音画质检测任务。

Input: 

```
tccli vod InspectMediaQuality --cli-unfold-argument  \
    --FileId 5285485487985271487 \
    --Definition 20001
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TaskId": "125xxx65-InspectMediaQuality-bffb15f07530b57bc1aabb01fac74bcc"
    }
}
```

