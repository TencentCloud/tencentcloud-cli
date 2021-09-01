**Example 1: 重设一个任务流模板的内容**

修改一个名为“我的一个任务流”的任务流模板，将任务流转码输出改成220，230，240三种格式。

Input: 

```
tccli vod ResetProcedureTemplate --cli-unfold-argument  \
    --Name 我的一个任务流 \
    --MediaProcessTask.TranscodeTaskSet.0.Definition 220 \
    --MediaProcessTask.TranscodeTaskSet.1.Definition 230 \
    --MediaProcessTask.TranscodeTaskSet.2.Definition 240
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3"
    }
}
```

