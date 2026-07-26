**Example 1: 删除一条出站规则**

删除一条出站互联网边界规则。

Input: 

```
tccli cfw RemoveAclRule --cli-unfold-argument  \
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

