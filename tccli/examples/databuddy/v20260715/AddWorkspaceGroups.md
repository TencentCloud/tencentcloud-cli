**Example 1: demo**

添加工作空间用户组

Input: 

```
tccli databuddy AddWorkspaceGroups --cli-unfold-argument  \
    --GroupIds 17613710998352474 \
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
        "RequestId": "fb139711-996b-44ba-9248-96696f0931c2"
    }
}
```

