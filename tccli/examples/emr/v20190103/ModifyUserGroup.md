**Example 1: 修改用户的用户组**



Input: 

```
tccli emr ModifyUserGroup --cli-unfold-argument  \
    --Users user1 \
    --UserGroup group4 \
    --Groups group4 \
    --Remark modify
```

Output: 
```
{
    "Response": {
        "RequestId": "43d2a958-6cdf-422b-903e-0bbf2aaa2619"
    }
}
```

