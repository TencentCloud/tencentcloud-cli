**Example 1: 创建AIGC视频转绘任务**

创建AIGC视频转绘任务

Input: 

```
tccli live CreateVideoRedrawTask --cli-unfold-argument  \
    --Input.Url https://****************.cos.ap-guangzhou.myqcloud.com/fod_1.mp4
```

Output: 
```
{
    "Response": {
        "TaskId": "d6f9bb2a-d1cd-****-447a-a4842e4279c6",
        "RequestId": "74ab0e9d-2b15-46ae-9c6c-042f360ae32b"
    }
}
```

