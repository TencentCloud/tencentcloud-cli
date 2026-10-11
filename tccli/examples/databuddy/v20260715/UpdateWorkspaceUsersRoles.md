**Example 1: demo**

修改工作空间用户角色

Input: 

```
tccli databuddy UpdateWorkspaceUsersRoles --cli-unfold-argument  \
    --UserUins 600000561778 \
    --WorkspaceId 17621416814092400 \
    --RoleIds 3001
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "d2fb6b6b-5319-440d-beb0-d92ea6af44e7"
    }
}
```

