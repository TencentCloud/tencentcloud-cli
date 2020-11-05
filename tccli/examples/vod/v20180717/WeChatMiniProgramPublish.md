**Example 1: Initiating a release on WeChat Mini Program task**

This example shows you how to initiate a release on WeChat Mini Program task for the video whose `fileId` is `5285485487985271487` with transcoding template ID 10.

Input: 

```
tccli vod WeChatMiniProgramPublish --cli-unfold-argument  \
    --FileId 5285485487985271487\
    --SourceDefinition 10
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

