**Example 1: 新建访问权限**

新建访问权限

Input: 

```
tccli bh CreateAcl --cli-unfold-argument  \
    --Name acl_test \
    --AllowDiskRedirect True \
    --AllowAnyAccount True \
    --AllowClipFileUp True \
    --AllowClipFileDown False \
    --AllowClipTextUp False \
    --AllowClipTextDown False \
    --AllowFileUp False \
    --AllowFileDown False \
    --AllowDiskFileUp False \
    --AllowDiskFileDown False \
    --AllowShellFileUp False \
    --AllowShellFileDown False \
    --AllowFileDel False \
    --DepartmentId 1 \
    --AllowAccessCredential True \
    --AllowKeyboardLogger False \
    --MaxAccessCredentialDuration 86400
```

Output: 
```
{
    "Response": {
        "Id": 16790787,
        "RequestId": "afaab2dd-23d2-4c40-8c6d-19e87dffa9d8"
    }
}
```

