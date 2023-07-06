**Example 1: 创建用户组**

创建用户组

Input: 

```
tccli ciam CreateUserGroup --cli-unfold-argument  \
    --UserStoreId xxx \
    --DisplayName xxx \
    --Description xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "xxx",
        "UserGroupId": "xxx"
    }
}
```

