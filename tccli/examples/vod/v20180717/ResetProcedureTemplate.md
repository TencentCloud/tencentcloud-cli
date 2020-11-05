**Example 1: Resetting a task flow template**

Modify a task flow template named "My Task Flow" to change its transcoding output to three formats of 220, 230, and 240.

Input: 

```
tccli vod ResetProcedureTemplate --cli-unfold-argument  \
    --Name 'My Task Flow'\
    --MediaProcessTask.TranscodeTaskSet.0.Definition 220\
    --MediaProcessTask.TranscodeTaskSet.1.Definition 230\
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

