**Example 1: CreateUserGroup**

添加用户组

Input: 

```
tccli bi CreateUserGroup --cli-unfold-argument  \
    --GroupName 测试用户组 \
    --Location 0 \
    --ParentId -1
```

Output: 
```
{
    "Response": {
        "RequestId": "7b8dad84-4285-4717-ac6d-5a76a29cb815"
    }
}
```

