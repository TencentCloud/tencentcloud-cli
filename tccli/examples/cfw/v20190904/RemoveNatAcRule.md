**Example 1: 按具体 ID 删除一条 NAT 出站规则**

按具体规则 ID 删除一条 NAT 出站规则。

Input: 

```
tccli cfw RemoveNatAcRule --cli-unfold-argument  \
    --RuleUuid 730001 \
    --Direction 0
```

Output: 
```
{
    "Response": {
        "RuleUuid": [
            730001
        ],
        "RequestId": "00000000-0000-4000-8000-000000000001"
    }
}
```

