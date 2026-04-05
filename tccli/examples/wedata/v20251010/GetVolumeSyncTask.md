**Example 1: 获取任务状态**



Input: 

```
tccli wedata GetVolumeSyncTask --cli-unfold-argument  \
    --JobId 6820251107222707048
```

Output: 
```
{
    "Response": {
        "Data": {
            "ErrorMsg": "",
            "JobId": "6820251107222707048",
            "Status": "COMPLETED"
        },
        "RequestId": "68113fe9-97c7-47b2-94e0-7f0fb28a208c"
    }
}
```

