**Example 1: 添加漏洞防御白名单**

添加漏洞防御白名单

Input: 

```
tccli cwp ModifyRaspRules --cli-unfold-argument  \
    --VulVulsIDs 1 18878 \
    --WhiteType 1
```

Output: 
```
{
    "Response": {
        "RequestId": "01d1e534-0292-4eac-9a95-746f0f6f60ad"
    }
}
```

