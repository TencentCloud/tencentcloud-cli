**Example 1: 创建账户组**



Input: 

```
tccli fwm CreateAccountGroup --cli-unfold-argument  \
    --GroupName 生产账号组 \
    --Description 生产账号组
```

Output: 
```
{
    "Response": {
        "GroupId": "acg-rwqqudnm",
        "RequestId": "a819e93f-ecf6-4ea0-8f85-1403562fc329"
    }
}
```

