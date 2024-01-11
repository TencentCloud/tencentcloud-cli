**Example 1: 验证已签名的可验证凭证**

验证凭证颁发者签发的可验证凭证

Input: 

```
tccli tdid VerifyCredentials --cli-unfold-argument  \
    --DAPId 1 \
    --CredentialData {"claim":{"age":18,"id":"did:tdid:w1:0x3b67623cbdaa9ccbfc8b7c346588c6bcbc6f5d63","name":"zhang san"},"context":"https://github.com/WeBankFinTech/WeIdentity/blob/master/context/v1","CPTId":12000000,"expirationDate":1871212353,"id":"42e180f9-e4fd-4cd0-93a6-1770f1f69c44","issuanceDate":1628063788,"issuer":"did:tdid:w1:0x4c59267a10ed54857842674d0c76ab708c6275f5","proof":{"created":1628063788,"creator":"did:tdid:w1:0x4c59267a10ed54857842674d0c76ab708c6275f5#keys-0","salt":{"age":"KeMT6","id":"qGZIB","name":"8jMxZ"},"signatureValue":"mf9UEjhh2gIpxr2evRh+zbC2/1k4YyxKl4otn2v96wQfNrz3MKQ+nsc0P0H/hFNlh3F+8Z1gN9qSemWXyN8KAwA=","type":"Secp256k1"},"type":["VerifiableCredential","original"]}
```

Output: 
```
{
    "Response": {
        "Result": true,
        "VerifyCode": 0,
        "VerifyMessage": "success",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

