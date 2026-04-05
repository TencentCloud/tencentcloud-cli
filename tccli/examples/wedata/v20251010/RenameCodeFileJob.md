**Example 1: 重命名执行记录**

重命名执行记录

Input: 

```
tccli wedata RenameCodeFileJob --cli-unfold-argument  \
    --WorkspaceId 1 \
    --CodeFileId 1 \
    --JobId 1 \
    --JobName 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "26b71e6a-c042-4b34-86b6-b763b7ab4073"
    }
}
```

