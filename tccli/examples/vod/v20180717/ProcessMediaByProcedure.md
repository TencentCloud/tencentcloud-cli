**Example 1: Initiating a task with task flow template name**

This example shows you how to initiate a task with the task flow template named `TranscodeAndSnapshot` for `fileId` 5285485487985271487.

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
        "TaskId": "125xxx65-procedurev2-bffb15f07530b57bc1aabb01fac74bca"
    }
}
```

