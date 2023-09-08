**Example 1: 删除互联网边界访问控制规则**

删除互联网边界访问控制规则

Input: 

```
tccli cfw RemoveAclRule --cli-unfold-argument  \
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
        "RequestId": "abc"
    }
}
```

