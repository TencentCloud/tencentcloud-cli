**Example 1: 发起智能去除水印任务**

对 FileId 为 5285485487985271487 的视频发起智能去除水印任务。

Input: 

```
tccli vod RemoveWatermark --cli-unfold-argument  \
    --FileId 5285485487985271487
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TaskId": "125xxx65-RemoveWatermark-bffb15f07530b57bc1aabb01fac74bca"
    }
}
```

