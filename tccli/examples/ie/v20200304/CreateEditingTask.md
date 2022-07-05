**Example 1: 创建智能编辑任务**

对一个视频进行标签识别

Input: 

```
tccli ie CreateEditingTask --cli-unfold-argument  \
    --DownInfo.UrlInfo.Url http://test.video.myqcloud.com/testA.mp4 \
    --DownInfo.Type 0 \
    --EditingInfo.TagEditingInfo.Switch 1
```

Output: 
```
{
    "Response": {
        "TaskId": "8E312055EBF7A503B92947E6D3B21EFF_1573715265075",
        "RequestId": "5z1993x8-05y9-14a8-ab55-192ff22297c9"
    }
}
```

