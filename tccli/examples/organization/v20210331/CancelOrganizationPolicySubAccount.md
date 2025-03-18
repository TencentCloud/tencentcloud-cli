**Example 1: 解绑成员访问授权策略和组织管理员子账号**



Input: 

```
tccli organization CancelOrganizationPolicySubAccount --cli-unfold-argument  \
    --PolicyId 123 \
    --OrgSubAccountUins 111111111111
```

Output: 
```
{
    "Response": {
        "RequestId": "ae4cbff0-b722-4ef1-b1b0-2088af894566"
    }
}
```

