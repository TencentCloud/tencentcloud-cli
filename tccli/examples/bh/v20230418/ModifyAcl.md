**Example 1: 修改访问权限**

修改访问权限

Input: 

```
tccli bh ModifyAcl --cli-unfold-argument  \
    --AllowClipTextUp True \
    --MaxFileDownSize 1 \
    --CmdTemplateIdSet 1 \
    --AllowFileDown True \
    --Name test-name \
    --UserGroupIdSet 1 \
    --DeviceGroupIdSet 1 \
    --AllowDiskRedirect True \
    --AllowClipFileUp True \
    --AccountSet root \
    --AllowAnyAccount True \
    --AllowClipFileDown True \
    --DeviceIdSet 1 \
    --AllowFileUp True \
    --MaxFileUpSize 1 \
    --UserIdSet 1 \
    --Id 1 \
    --AllowClipTextDown True
```

Output: 
```
{
    "Response": {
        "RequestId": "ec7676f4-a498-4ef5-ad68-6678b16e45d7"
    }
}
```

