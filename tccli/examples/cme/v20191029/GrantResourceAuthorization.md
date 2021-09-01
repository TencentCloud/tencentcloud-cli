**Example 1: 发起媒资授权**



Input: 

```
tccli cme GrantResourceAuthorization --cli-unfold-argument  \
    --Platform test \
    --Operator 123 \
    --Permissions R \
    --Owner.Type PERSON \
    --Owner.Id 123 \
    --Resources.0.Type MATERIAL \
    --Resources.0.Id mid_abc \
    --Authorizees.0.Type TEAM \
    --Authorizees.0.Id teamA
```

Output: 
```
{
    "Response": {
        "RequestId": "requestId"
    }
}
```

