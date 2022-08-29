**Example 1: 查询访问权限列表**



Input: 

```
tccli dasb DescribeAcls --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AclSet": [
            {
                "Id": 224,
                "Name": "云鼎部门权限",
                "AllowDiskRedirect": true,
                "AllowDiskFileUp": true,
                "AllowDiskFileDown": true,
                "AllowClipFileUp": true,
                "AllowClipFileDown": true,
                "AllowClipTextUp": true,
                "AllowClipTextDown": true,
                "AllowShellFileUp": true,
                "AllowShellFileDown": true,
                "AllowFileUp": true,
                "AllowFileDown": true,
                "AllowFileDel": false,
                "MaxFileUpSize": 0,
                "MaxFileDownSize": 0,
                "AllowAnyAccount": false,
                "ValidateFrom": "1970-01-01T08:00:01+08:00",
                "ValidateTo": "1970-01-01T08:00:01+08:00",
                "Status": 1,
                "UserSet": [],
                "UserGroupSet": [],
                "DeviceSet": [],
                "DeviceGroupSet": [],
                "AccountSet": [],
                "CmdTemplateSet": [],
                "Department": {
                    "Id": "1.3.14",
                    "Name": "云鼎实验室",
                    "Managers": null
                }
            }
        ],
        "RequestId": "aba1efad-4aa2-4ce4-93ce-538e39b5f1f9",
        "TotalCount": 1
    }
}
```

**Example 2: 根据用户和主机查询对应的权限**

根据用户和主机查询对应的权限

Input: 

```
tccli dasb DescribeAcls --cli-unfold-argument  \
    --AuthorizedUserIdSet 1 7 8 238 \
    --AuthorizedDeviceIdSet 63 64 82 100
```

Output: 
```
{
    "Response": {
        "AclSet": [
            {
                "Id": 224,
                "Name": "云鼎部门权限",
                "AllowDiskRedirect": true,
                "AllowDiskFileUp": true,
                "AllowDiskFileDown": true,
                "AllowClipFileUp": true,
                "AllowClipFileDown": true,
                "AllowClipTextUp": true,
                "AllowClipTextDown": true,
                "AllowShellFileUp": true,
                "AllowShellFileDown": true,
                "AllowFileUp": true,
                "AllowFileDown": true,
                "AllowFileDel": false,
                "MaxFileUpSize": 0,
                "MaxFileDownSize": 0,
                "AllowAnyAccount": false,
                "ValidateFrom": "1970-01-01T08:00:01+08:00",
                "ValidateTo": "1970-01-01T08:00:01+08:00",
                "Status": 1,
                "UserSet": [],
                "UserGroupSet": [],
                "DeviceSet": [],
                "DeviceGroupSet": [],
                "AccountSet": [],
                "CmdTemplateSet": [],
                "Department": {
                    "Id": "1.3.14",
                    "Name": "云鼎实验室",
                    "Managers": null
                }
            }
        ],
        "RequestId": "aba1efaa-4ac2-4ce3-93ce-538539b5f1f9",
        "TotalCount": 1
    }
}
```

