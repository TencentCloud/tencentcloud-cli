**Example 1: 新建访问权限**

新建访问权限

Input: 

```
tccli dasb CreateAcl --cli-unfold-argument  \
    --CmdTemplateIdSet 1 \
    --Name test-name \
    --UserGroupIdSet 1 \
    --DeviceGroupIdSet 1 \
    --AllowDiskRedirect True \
    --AccountSet root \
    --AllowAnyAccount True \
    --DeviceIdSet 1 \
    --UserIdSet 1
```

Output: 
```
{
    "Response": {
        "Id": 1,
        "RequestId": "dfac9070-8b23-499e-83b2-a50e3ca059af"
    }
}
```

