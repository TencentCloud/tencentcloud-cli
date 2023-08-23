**Example 1: 查询防护墙模板规则配额**

查询防护墙模板规则配额

Input: 

```
tccli lighthouse DescribeFirewallTemplateRuleQuota --cli-unfold-argument  \
    --TemplateId lhft-6brh0ciy
```

Output: 
```
{
    "Response": {
        "Available": 98,
        "RequestId": "1a73f3ef-9098-4537-89af-90f59a49abb8",
        "Total": 100
    }
}
```

