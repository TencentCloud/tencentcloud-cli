**Example 1: 更新访问凭证权限为读写**

修改访问凭证的权限为读写

Input: 

```
tccli tcr UpdateApplicationTokenPermissionPersonal --cli-unfold-argument  \
    --Readonly False
```

Output: 
```
{
    "Response": {
        "RequestId": "5d6a8c75-ae78-49d0-ace2-91033a8dffc3"
    }
}
```

**Example 2: 更新访问凭证权限为只读**

修改访问凭证的权限为只读

Input: 

```
tccli tcr UpdateApplicationTokenPermissionPersonal --cli-unfold-argument  \
    --Readonly True
```

Output: 
```
{
    "Response": {
        "RequestId": "ec338283-91b9-40c2-a9a6-4593b1362951"
    }
}
```

