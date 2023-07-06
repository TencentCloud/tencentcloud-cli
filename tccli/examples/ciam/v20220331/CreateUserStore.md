**Example 1: 创建用户目录**

创建用户目录

Input: 

```
tccli ciam CreateUserStore --cli-unfold-argument  \
    --UserPoolName abc \
    --UserPoolDesc abc \
    --UserPoolLogo abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc",
        "UserStoreId": "abc"
    }
}
```

