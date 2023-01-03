**Example 1: 以任务流模板名的方式发起任务**

对 fileId 为 5285485487985271487 的发起任务，使用的任务流模板名为 TranscodeAndSnapshot。

Input: 

```
tccli vod ProcessMediaByProcedure --cli-unfold-argument  \
    --FileId 5285485487985271487 \
    --ProcedureName TranscodeAndSnapshot
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TaskId": "125xxx65-procedurev2-bffb15f07530b57bc1aabb01fac74bca",
        "ReviewAudioVideoTaskId": ""
    }
}
```

