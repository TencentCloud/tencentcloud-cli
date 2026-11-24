**Example 1: 示例1**



Input: 

```
tccli bh ApproveTicket --cli-unfold-argument  \
    --Id 1 \
    --Status 4 \
    --ApproveDesc  \
    --ApplyTimeVersion 0 \
    --AllowDiskRedirect True \
    --AllowClipFileUp True \
    --AllowClipFileDown True \
    --AllowClipTextUp True \
    --AllowClipTextDown True \
    --AllowFileUp True \
    --MaxFileUpSize 1 \
    --AllowFileDown True \
    --MaxFileDownSize 1 \
    --AllowDiskFileUp True \
    --AllowDiskFileDown True \
    --AllowShellFileUp True \
    --AllowShellFileDown True \
    --AllowFileDel True \
    --AllowAccessCredential True \
    --CmdTemplateIdSet 1 \
    --ACTemplateIdSet 1 \
    --DepartmentId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "ec7676f4-a498-4ef5-ad68-6678b16e45d7"
    }
}
```

