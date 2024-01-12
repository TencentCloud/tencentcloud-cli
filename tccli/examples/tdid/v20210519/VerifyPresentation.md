**Example 1: 验证可验证凭证表达**



Input: 

```
tccli tdid VerifyPresentation --cli-unfold-argument  \
    --Did did:tdid:w1:0xc1f030ceeb858887f0cc400030d59534cf8098c8 \
    --PresentationData {"context":["https://github.com/TencentCloud-Blockchain/TDID/blob/main/context/v1"],"holder":"did:tdid:w1:0xc1f030ceeb858887f0cc400030d59534cf8098c8","proof":{"created":"2023-09-12T16:14:56+08:00","nonce":"test","signatureValue":"MEYCIQC4Wmf0NTlNF9BOjyynLasqWQJF4M34oIiemCa2Jl6+1wIhANqKc4/sWbuQmcpp7ilNrpfZQU4Cj0+VqcQcN+/jZH5u","type":"Secp256r1","verificationMethod":"did:tdid:w1:0xc1f030ceeb858887f0cc400030d59534cf8098c8#keys-0"},"type":["VerifiablePresentation"],"verifiableCredential":[{"context":"https://github.com/TencentCloud-Blockchain/TDID/blob/main/context/v1","cptId":1,"credentialSubject":{"action":"deactiveDid","age":"0x7cc931132828080cac176a6bf266077bc963d3a8d4afacb147eb7a5fa9d38176","ageCommitment":"/nQps1EGGKMJEEIZhlNu9oFZWTSe6bR5e2w71+/JSgE="},"expirationDate":"2024-06-29T15:25:00+08:00","id":"0971a8c6a1ff17d9b85abaab5e02c50d","issuanceDate":"2023-09-12T15:50:52+08:00","issuer":"did:tdid:w1:0xc1f030ceeb858887f0cc400030d59534cf8098c8","proof":{"created":"2023-09-12T15:50:52+08:00","creator":"did:tdid:w1:0xc1f030ceeb858887f0cc400030d59534cf8098c8#keys-0","metaDigest":"da11a3571b4920ebdac1b73b03c696606a3b1c380e6502bcb30484d8240ae28d","privacy":"Public","salt":{"action":"0UU2V","age":"0","ageCommitment":"XiqAq"},"signatureValue":"MEQCIHGw37fwROCoqUEz9Rtw2CG3pQP6QYxe2byS45LIlPBmAiBrS93DNqRtVYKUq8dZ4ZUTSgt9Ajr9rzqLB3KZz9ADIg==","type":"Secp256r1","vcDigest":"230653978a8dc2c16f6acfa7bfb779a34d282fb7fd2eae5646c9e3ba95589344"},"type":["VerifiableCredential"]}]} \
    --DAPId 1 \
    --VerifyCode test
```

Output: 
```
{
    "Response": {
        "Result": true,
        "VerifyCode": 0,
        "VerifyMessage": "success",
        "RequestId": "1b5c5ee5-a049-4137-8ca1-f4337a614d91"
    }
}
```

