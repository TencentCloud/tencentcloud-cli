**Example 1: 对点播中的一个文件进行拆条，生成两个新的视频**



Input: 

```
tccli vod SplitMedia --cli-unfold-argument  \
    --FileId 5285485487985271487 \
    --Segments.0.StartTimeOffset 40.0 \
    --Segments.0.EndTimeOffset 50.0 \
    --Segments.1.StartTimeOffset 60.0 \
    --Segments.1.EndTimeOffset 70.0
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TaskId": "125xxx65-SplitMedia-bffb15f07530b57bc1aabb01fac74bca"
    }
}
```

