**Example 1: 创建PPT检测任务**

创建PPT检测任务，识别动态转码不支持的元素列表

Input: 

```
tccli tiw CreatePPTCheckTask --cli-unfold-argument  \
    --Url http://example.com/%E6%B5%8B%E8%AF%95.pptx \
    --SdkAppId 1400000001
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "TaskId": "g6ls63ps49vteb8bk1mb"
    }
}
```

