**Example 1: 发起小程序视频发布任务**

对 fileId 为 5285485487985271487 的视频发起微信小程序发布任务，且发布视频所对应的转码模板 ID 为 100030。

Input: 

```
tccli vod WeChatMiniProgramPublish --cli-unfold-argument  \
    --FileId 5285485487985271487 \
    --SourceDefinition 100030
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TaskId": "125xxx65-wechat-mini-program-publish-bffb15f07530b57bc1aabb01fac74bca"
    }
}
```

