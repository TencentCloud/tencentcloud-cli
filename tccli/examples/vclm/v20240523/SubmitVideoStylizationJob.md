**Example 1: 成功提交任务**

成功提交视频风格化任务

Input: 

```
tccli vclm SubmitVideoStylizationJob --cli-unfold-argument  \
    --StyleId 2d_anime \
    --VideoUrl https://cos.ap-guangzhou.myqcloud.com/video.mp4 \
    --StyleStrength medium
```

Output: 
```
{
    "Response": {
        "JobId": "c5daf8f7077d41a69c13aab31a7164f3",
        "RequestId": "b1990ba2-2d71-419d-8c9d-cab8e33f8352"
    }
}
```

