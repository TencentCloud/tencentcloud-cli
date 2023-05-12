**Example 1: 修改访问权限**

修改访问权限

Input: 

```
tccli dasb ModifyAcl --cli-unfold-argument  \
    --AllowClipTextUp True \
    --MaxFileDownSize 1 \
    --CmdTemplateIdSet 1 \
    --AllowFileDown True \
    --Name abc \
    --UserGroupIdSet 1 \
    --DeviceGroupIdSet 1 \
    --AllowDiskRedirect True \
    --AllowClipFileUp True \
    --AccountSet aaa \
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
        "RequestId": "abcd12321aax"
    }
}
```

