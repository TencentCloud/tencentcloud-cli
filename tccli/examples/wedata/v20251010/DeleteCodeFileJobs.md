**Example 1: 删除执行记录**

删除执行记录

Input: 

```
tccli wedata DeleteCodeFileJobs --cli-unfold-argument  \
    --WorkspaceId 17623497097012366 \
    --CodeFileId 794235159865778176 \
    --JobIds job_2
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "edadd425-6fd3-4371-8718-e145413875e9"
    }
}
```

