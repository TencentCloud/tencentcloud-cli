**Example 1: 续期 MCP Token**

用于延长 Token 过期时间

Input: 

```
tccli car RenewMCPToken --cli-unfold-argument  \
    --TokenId tok_532*******6babb3 \
    --ExpireSeconds 604800
```

Output: 
```
{
    "Response": {
        "RequestId": "3bb0741a-897e-456c-a553-c0bd9e4d5596"
    }
}
```

