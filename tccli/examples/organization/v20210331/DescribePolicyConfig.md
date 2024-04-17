**Example 1: 查看企业组织策略配置**

查看企业组织策略配置

Input: 

```
tccli organization DescribePolicyConfig --cli-unfold-argument  \
    --OrganizationId 80001
```

Output: 
```
{
    "Response": {
        "RequestId": "20678896-12d1-11ed-a2cd-525400fed39d",
        "Status": 1,
        "Type": "SERVICE_CONTROL_POLICY"
    }
}
```

