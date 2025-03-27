**Example 1: 发起媒资授权**



Input: 

```
tccli cme GrantResourceAuthorization --cli-unfold-argument  \
    --Authorizees.0.Type TEAM \
    --Authorizees.0.Id teamA \
    --Platform 1000000009 \
    --Operator cmeid_system \
    --Owner.Type PERSON \
    --Owner.Id aa2b2421-425f-435d-b580-d417bdd73dd8 \
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

