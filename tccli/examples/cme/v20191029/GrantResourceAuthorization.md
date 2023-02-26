**Example 1: 发起媒资授权**



Input: 

```
tccli cme GrantResourceAuthorization --cli-unfold-argument  \
    --Authorizees.0.Type TEAM \
    --Authorizees.0.Id teamA \
    --Platform test \
    --Operator 123 \
    --Owner.Type PERSON \
    --Owner.Id 123 \
    --Resources.0.Type MATERIAL \
    --Resources.0.Id mid_abc \
    --Permissions R
```

Output: 
```
{
    "Response": {
        "RequestId": "d1c5eb0e-e499-4419-b465-60c0973b3d2"
    }
}
```

