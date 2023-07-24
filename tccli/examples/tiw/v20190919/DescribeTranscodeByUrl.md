**Example 1: 通过url查询文档动态转码任务状态**

通过url查询文档动态转码任务状态

Input: 

```
tccli tiw DescribeTranscodeByUrl --cli-unfold-argument  \
    --Url https://path/to/document.ppt \
    --SdkAppId 1400000001
```

Output: 
```
{
    "Response": {
        "Progress": 100,
        "RequestId": "d290f1ee-6c54-4b01-90e6-d701748f0851",
        "Status": "FINISHED",
        "TaskId": "0agdnligqtgtvkm65emb"
    }
}
```

