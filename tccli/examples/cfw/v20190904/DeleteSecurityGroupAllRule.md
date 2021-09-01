**Example 1: 删除全部安全组规则**



Input: 

```
tccli cfw DeleteSecurityGroupAllRule --cli-unfold-argument  \
    --Area ap-guangzhou \
    --Direction 0
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "Info": "",
        "RequestId": "b21d7f7c-3191-41a2-bd13-9a5f6d86ab44"
    }
}
```

