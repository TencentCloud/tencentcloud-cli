**Example 1: 删除NAT访问控制规则**

删除NAT访问控制规则

Input: 

```
tccli cfw RemoveNatAcRule --cli-unfold-argument  \
    --RuleUuid 0 \
    --Direction 1
```

Output: 
```
{
    "Response": {
        "RuleUuid": [
            0
        ],
        "RequestId": "xx"
    }
}
```

