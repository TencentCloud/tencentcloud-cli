**Example 1: 新建访问权限**

新建访问权限

Input: 

```
tccli dasb CreateAcl --cli-unfold-argument  \
    --CmdTemplateIdSet 1 \
    --Name abc \
    --UserGroupIdSet 1 \
    --DeviceGroupIdSet 1 \
    --AllowDiskRedirect True \
    --AccountSet abc \
    --AllowAnyAccount True \
    --DeviceIdSet 1 \
    --UserIdSet 1
```

Output: 
```
{
    "Response": {
        "Id": 1,
        "RequestId": "31jshapqhxmajh12knskal2"
    }
}
```

