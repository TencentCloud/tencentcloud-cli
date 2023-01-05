**Example 1: 提取溯源水印**

用于提取溯源水印。

Input: 

```
tccli vod ExtractTraceWatermark --cli-unfold-argument  \
    --Url http://example.com/path/file.mp4 \
    --FileId 123422
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TaskId": "125xxx65-procedurev2-bffb15f07530b57bc1aabb01fac74bca"
    }
}
```

