**Example 1: 创建用户目录**

创建用户目录

Input: 

```
tccli ciam CreateUserStore --cli-unfold-argument  \
    --UserPoolName 目录1 \
    --UserPoolDesc 管理应用和用户 \
    --UserPoolLogo https://aa.com/bb.png
```

Output: 
```
{
    "Response": {
        "UserStoreId": "2c3aca3b****************a7efe88e",
        "RequestId": "e2e9e8aa********************9ab34c6e"
    }
}
```

