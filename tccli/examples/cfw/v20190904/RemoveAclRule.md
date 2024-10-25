**Example 1: 删除互联网边界访问控制规则**

删除互联网边界访问控制规则

Input: 

```
tccli cfw RemoveAclRule --cli-unfold-argument  \
    --RuleUuid 100 \
    --Direction 1
```

Output: 
```
{
    "Response": {
        "RuleUuid": [
            100
        ],
        "RequestId": "3cfe92c5-da49-411e-9254-559a295471e9"
    }
}
```

