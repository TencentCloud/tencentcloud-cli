**Example 1: 输入普通话新闻素材，发起智能标签任务**



Input: 

```
tccli ivld CreateTask --cli-unfold-argument  \
    --MediaPreknownInfo.MediaLang 1 \
    --MediaPreknownInfo.MediaSecondLabel 0 \
    --MediaPreknownInfo.MediaLabel 1 \
    --MediaPreknownInfo.MediaType 2 \
    --TaskName demo-task-0 \
    --MediaId media-a1b2c3d4 \
    --UploadVideo False
```

Output: 
```
{
    "Response": {
        "RequestId": "2713de41-b294-429b-ac13-2c3f5c49b1db",
        "TaskId": "task-g8lqk737"
    }
}
```

