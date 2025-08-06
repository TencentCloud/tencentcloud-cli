**Example 1: 验证第三方应用访问凭证**



Input: 

```
tccli tcr ValidateApplicationTokenPersonal --cli-unfold-argument  \
    --ApplicationToken {ApplicationToken:1sadfasdfsad34234dfadrfqwerqwr}
```

Output: 
```
{
    "Response": {
        "RequestId": "79cf7b19-4ec9-4cb9-a521-2b7b29eacf29",
        "Data": true
    }
}
```

