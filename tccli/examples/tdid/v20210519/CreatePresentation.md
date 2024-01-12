**Example 1: 创建可验证表达**



Input: 

```
tccli tdid CreatePresentation --cli-unfold-argument  \
    --DAPId 1 \
    --CredentialList.0.Credential {"cptId":1,"issuer":"did:tdid:w1:0x379106c7232aed1a50e8600511655b479c76b149","expirationDate":"2124-06-29T15:25:00+08:00","issuanceDate":"2023-11-30T05:19:40+08:00","context":"https://github.com/TencentCloud-Blockchain/TDID/blob/main/context/v1","id":"0767cc1f93ad541e195bd9f5f00d665f","type":["VerifiableCredential"],"credentialSubject":{"action":"deactiveDid","age":17},"proof":{"created":"2023-11-30T05:19:40+08:00","creator":"did:tdid:w1:0x379106c7232aed1a50e8600511655b479c76b149#keys-0","signatureValue":"MEQCIEWnreXh0siSPnCaAqCldL1E+gTdrT6oSZjbTjAhwn6+AiBXn/ZIirpr69JknKsX3+MWRE7WeIXGdaOIXY10c36hoA==","type":"Secp256r1","metaDigest":"7d6435235cd5afdb7abd06a979eb2237d103401bdb54fa38ff6b8299c7529b76","vcDigest":"d014b006648f48e13c1aff9c16a39979e3d17e6f32c816065158d6a92632a132","privacy":"Public","salt":{"action":"YuzFn","age":"0zche"}}} \
    --Did did:tdid:w1:0xc1f030ceeb858887f0cc400030d59534cf8098c8 \
    --VerifyCode test \
    --PolicyJson {"1":{"age":0}}
```

Output: 
```
{
    "Response": {
        "PresentationData": "{\"context\":[\"https://github.com/TencentCloud-Blockchain/TDID/blob/main/context/v1\"],\"holder\":\"did:tdid:c2:0x379106c7232aed1a50e8600511655b479c76b149\",\"proof\":{\"created\":\"2024-01-08T15:17:00+08:00\",\"nonce\":\"test\",\"signatureValue\":\"eyJjb250ZXh0IjpbImh0dHBzOi8vZ2l0aHViLmNvbS9UZW5jZW50Q2xvdWQtQmxvY2tjaGFpbi9URElEL2Jsb2IvbWFpbi9jb250ZXh0L3YxIl0sImhvbGRlciI6ImRpZDp0ZGlkOmMyOjB4Mzc5MTA2YzcyMzJhZWQxYTUwZTg2MDA1MTE2NTViNDc5Yzc2YjE0OSIsInR5cGUiOlsiVmVyaWZpYWJsZVByZXNlbnRhdGlvbiJdLCJ2ZXJpZmlhYmxlQ3JlZGVudGlhbCI6W3siY29udGV4dCI6Imh0dHBzOi8vZ2l0aHViLmNvbS9UZW5jZW50Q2xvdWQtQmxvY2tjaGFpbi9URElEL2Jsb2IvbWFpbi9jb250ZXh0L3YxIiwiY3B0SWQiOjEsImNyZWRlbnRpYWxTdWJqZWN0Ijp7ImFjdGlvbiI6ImRlYWN0aXZlRGlkIiwiYWdlIjoiMHg5NzUwNWE0ODY0NzM0NzBlNTBkMTM3MzIzMTM3ZGE4NTE3M2Y5OGU4MzQ0MGEzYjhjMWE3M2Q2ZDI0YWRiNmZlIn0sImV4cGlyYXRpb25EYXRlIjoiMjEyNC0wNi0yOVQxNToyNTowMCswODowMCIsImlkIjoiOGNmZTc1ZjFlMjlkOTk4ZWRhZGI5NjFlMTQxMDEyOWUiLCJpc3N1YW5jZURhdGUiOiIyMDI0LTAxLTA4VDEwOjM3OjU0KzA4OjAwIiwiaXNzdWVyIjoiZGlkOnRkaWQ6YzI6MHgzNzkxMDZjNzIzMmFlZDFhNTBlODYwMDUxMTY1NWI0NzljNzZiMTQ5IiwicHJvb2YiOnsiY3JlYXRlZCI6IjIwMjQtMDEtMDhUMTA6Mzc6NTQrMDg6MDAiLCJjcmVhdG9yIjoiZGlkOnRkaWQ6YzI6MHgzNzkxMDZjNzIzMmFlZDFhNTBlODYwMDUxMTY1NWI0NzljNzZiMTQ5I2tleXMtMCIsIm1ldGFEaWdlc3QiOiJiNGE2ODVjMzQ0ZGViMjg1Y2IwMTFiYzhiNmI3Mjg3NzhmYmU0NmNhOWZhYTE4OGNlYTZkYmM5YzM2ZDNiZDFiIiwicHJpdmFjeSI6IlB1YmxpYyIsInNhbHQiOnsiYWN0aW9uIjoieDZQMG4iLCJhZ2UiOiIwIn0sInNpZ25hdHVyZVZhbHVlIjoiTUVVQ0lFWEJkd2tHRi85UXpkdDRPRzlHS2cyRUJEb1hFOTAySGNFdlVndXMvbTZ3QWlFQW1NU3lRS0F1SUZvYmI4cTNDWkJTRmdBczhZL09WdEMwNTN0VVJTRk5SREk9IiwidHlwZSI6IlNlY3AyNTZyMSIsInZjRGlnZXN0IjoiMmRkNWExZGMzMjQ2ODZjOTNhNWIxNTgyMDZkNWZlOGI5MzdhMWZlNjQ3NjA5ODNkNWY1OWIyMzcxY2RlYjA5NSJ9LCJ0eXBlIjpbIlZlcmlmaWFibGVDcmVkZW50aWFsIl19XX0=\",\"type\":\"Secp256r1\",\"verificationMethod\":\"did:tdid:c2:0x379106c7232aed1a50e8600511655b479c76b149#keys-0\",\"vpDigest\":\"6728c750e86b1b793878c2a281bbebbe8d08b06a9266c1588ef841c6b3768475\"},\"type\":[\"VerifiablePresentation\"],\"verifiableCredential\":[{\"context\":\"https://github.com/TencentCloud-Blockchain/TDID/blob/main/context/v1\",\"cptId\":1,\"credentialSubject\":{\"action\":\"deactiveDid\",\"age\":\"0x97505a486473470e50d137323137da85173f98e83440a3b8c1a73d6d24adb6fe\"},\"expirationDate\":\"2124-06-29T15:25:00+08:00\",\"id\":\"8cfe75f1e29d998edadb961e1410129e\",\"issuanceDate\":\"2024-01-08T10:37:54+08:00\",\"issuer\":\"did:tdid:c2:0x379106c7232aed1a50e8600511655b479c76b149\",\"proof\":{\"created\":\"2024-01-08T10:37:54+08:00\",\"creator\":\"did:tdid:c2:0x379106c7232aed1a50e8600511655b479c76b149#keys-0\",\"metaDigest\":\"b4a685c344deb285cb011bc8b6b728778fbe46ca9faa188cea6dbc9c36d3bd1b\",\"privacy\":\"Public\",\"salt\":{\"action\":\"x6P0n\",\"age\":\"0\"},\"signatureValue\":\"MEUCIEXBdwkGF/9Qzdt4OG9GKg2EBDoXE902HcEvUgus/m6wAiEAmMSyQKAuIFobb8q3CZBSFgAs8Y/OVtC053tURSFNRDI=\",\"type\":\"Secp256r1\",\"vcDigest\":\"2dd5a1dc324686c93a5b158206d5fe8b937a1fe64760983d5f59b2371cdeb095\"},\"type\":[\"VerifiableCredential\"]}]}",
        "RequestId": "52163044-3cd1-4ca9-8963-a36ac5554364"
    }
}
```

