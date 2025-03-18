**Example 1: 绑定成员访问授权策略和组织管理员子账号**

绑定成员访问授权策略和组织管理员子账号

Input: 

```
tccli organization BindOrganizationPolicySubAccount --cli-unfold-argument  \
    --PolicyId 123 \
    --OrgSubAccountUins 111111111111
```

Output: 
```
{
    "Response": {
        "RequestId": "bebe4b80-bca5-45fe-a460-455045879f89"
    }
}
```

