**Example 1: 删除用户组成员**

删除用户组成员

Input: 

```
tccli bh DeleteUserGroupMembers --cli-unfold-argument  \
    --Id 1 \
    --MemberIdSet 1 2 3
```

Output: 
```
{
    "Response": {
        "RequestId": "c7c79e35-65b9-4c2a-beea-a038fdf8c082"
    }
}
```

