**Example 1: demo**



Input: 

```
tccli wedata CloneWorkspaceRole --cli-unfold-argument  \
    --WorkspaceId 1 \
    --SrcRoleId 3001 \
    --DstBasicInfo.Id 12457 \
    --DstBasicInfo.Name abe \
    --DstBasicInfo.Description abe \
    --DstBasicInfo.DisplayName abe
```

Output: 
```
{
    "Response": {
        "Data": {
            "RoleId": "784448714810134528"
        },
        "RequestId": "dcb6fb45-c921-4abd-95aa-1cd5d2673921"
    }
}
```

