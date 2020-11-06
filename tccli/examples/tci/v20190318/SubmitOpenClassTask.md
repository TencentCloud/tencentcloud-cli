**Example 1: 提交线下小班（学生无课桌遮挡场景）课任务**

提交线下小班（学生无课桌遮挡场景）课任务，选择视频资源文件类型进行评估。

Input: 

```
tccli tci SubmitOpenClassTask --cli-unfold-argument  \
    --FileContent https%3A%2F%2Fedu-test-1253131631.cos.ap-guangzhou.myqcloud.com%2Faieduautotest%2Fautotest_vedio.mp4 \
    --FileType vod_url \
    --LibrarySet library_15603955264181591716
```

Output: 
```
{
    "Response": {
        "TaskId": 2516205217,
        "ImageResults": null,
        "RequestId": "82d23aac-ff81-4821-bd58-99d2caf6136f"
    }
}
```

