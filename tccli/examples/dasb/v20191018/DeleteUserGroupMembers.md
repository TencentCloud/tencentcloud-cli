**Example 1: 删除用户组成员**

删除用户组成员

Input: 

```
tccli dasb DeleteUserGroupMembers --cli-unfold-argument  \
    --Id 1 \
    --MemberIdSet 1 2 3
```

Output: 
```
{
    "Response": {
        "RequestId": "f1a896ea-cbcf-4b4f-9e05-7ffedaa0f7c7"
    }
}
```

