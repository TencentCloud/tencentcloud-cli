**Example 1: 查询角色是否存在**



Input: 

```
tccli lighthouse DescribeServiceLinkedRoleExist --cli-unfold-argument  \
    --RoleName xxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "2b4afc89-4695-4832-96f9-a222517ab923",
        "Exist": true
    }
}
```

