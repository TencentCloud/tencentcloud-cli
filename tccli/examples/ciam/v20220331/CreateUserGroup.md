**Example 1: 创建用户组**

创建用户组

Input: 

```
tccli ciam CreateUserGroup --cli-unfold-argument  \
    --DisplayName 用户组1 \
    --Description 包含了一组用户 \
    --UserStoreId 2c3aca3b****************a7efe88e
```

Output: 
```
{
    "Response": {
        "UserGroupId": "6cd22e51****************f6f7cb81",
        "RequestId": "e2e9e8aa********************9ab34c6e"
    }
}
```

