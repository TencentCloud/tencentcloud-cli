**Example 1: VerifyCredential**

验证凭证

Input: 

```
tccli tdid VerifyCredential --cli-unfold-argument  \
    --FunctionArg.ClaimJson {"name": "zhang san", "id": "did:tdid:15:0x3b67623cbdaa9ccbfc8b7c346588c6bcbc6f5d63", "age": 18} \
    --FunctionArg.CptId 2000000 \
    --FunctionArg.ExpirationDate 1871212353 \
    --FunctionArg.Context https://github.com/WeBankFinTech/WeIdentity/blob/master/context/v1 \
    --FunctionArg.Proof.SignatureValue IL/CtZKrg+g395nYZbXT/Uzk1N3/NG/tgjbjeMf03shcGl7jSRXgVk3zz+x5zp11OBApb43By6VjWdPUJJLJMQA= \
    --FunctionArg.Proof.Created 1627803566 \
    --FunctionArg.Proof.Type Secp256k1 \
    --FunctionArg.Proof.SaltJson {"age":"o58g1","id":"X5efp","name":"pu2UZ"} \
    --FunctionArg.Proof.Creator 1627803566 \
    --FunctionArg.Id 9bff9f22-2794-4d1e-b598-894163392cd9 \
    --FunctionArg.Type VerifiableCredential original \
    --FunctionArg.IssuanceDate 1627803566 \
    --FunctionArg.Issuer did:tdid:15:0x4c59267a10ed54857842674d0c76ab708c6275f5
```

Output: 
```
{
    "Response": {
        "Result": true,
        "VerifyCode": 0,
        "VerifyMessage": "success",
        "RequestId": "72a6643f-7123-4288-9584-8dd4db7e8373"
    }
}
```

