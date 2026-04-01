**Example 1: 终止CodeFileJob**

终止CodeFileJob

Input: 

```
tccli wedata TerminateCodeFileJob --cli-unfold-argument  \
    --WorkspaceId 17623497097012366 \
    --CodeFileId 794235159865778176 \
    --JobId job_2
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": false
        },
        "RequestId": "a9508f9f-f12c-42b7-b2e4-b3ac979600f7"
    }
}
```

