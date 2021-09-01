**Example 1: 新增图片类型样本**

将一张图片新增到样本库中，标注为色情

Input: 

```
tccli cms CreateFileSample --cli-unfold-argument  \
    --EvilType 20002 \
    --Label 1 \
    --FileType image \
    --Contents.0.FileName 苍老师.jpg \
    --Contents.0.FileUrl http://example.com/q.jpg \
    --Contents.0.FileMd5 9cc56fe973ec99c1f03afcc920df3a0b
```

Output: 
```
{
    "Response": {
        "RequestId": "c1935701-668a-4e0f-9f25-7e88a5f3f7af",
        "Progress": 2
    }
}
```

