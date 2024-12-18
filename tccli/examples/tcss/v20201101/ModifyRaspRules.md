**Example 1: 添加漏洞防御白名单**

添加漏洞防御白名单

Input: 

```
tccli tcss ModifyRaspRules --cli-unfold-argument  \
    --VulVulsIDs 105346 \
    --WhiteType 1
```

Output: 
```
{
    "Response": {
        "RequestId": "e8ff031f-094b-485d-949f-8b557b4d1b6d"
    }
}
```

