**Example 1: 修改访问权限**

修改访问权限

Input: 

```
tccli dasb ModifyAcl --cli-unfold-argument  \
    --AllowClipTextUp True \
    --MaxFileDownSize 1 \
    --CmdTemplateIdSet 1 \
    --AllowFileDown True \
    --Name 主机权限 \
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
        "RequestId": "dfac9070-8b23-499e-83b2-a50e3ca059af"
    }
}
```

