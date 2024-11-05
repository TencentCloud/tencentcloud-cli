**Example 1: 删除NAT访问控制规则**

删除NAT访问控制规则

Input: 

```
tccli cfw RemoveNatAcRule --cli-unfold-argument  \
    --RuleUuid 241996 \
    --Direction 1
```

Output: 
```
{
    "Response": {
        "RuleUuid": [
            241996
        ],
        "RequestId": "896b6a81-26f9-47d6-97c5-9fa14a7cc883"
    }
}
```

