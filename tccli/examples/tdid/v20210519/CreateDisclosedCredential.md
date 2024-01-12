**Example 1: 创建选择性披露凭证**

根据批量策略把可验证凭证转换成选择性披露凭证

Input: 

```
tccli tdid CreateDisclosedCredential --cli-unfold-argument  \
    --DAPId 41 \
    --CredentialData {"claim":{"action":"SetCredentialStatus","credentialStatus":{"credentialId":"0d8062f09bff4eb5b9697d1de28eebda","issuer":"did:tdid:w1:0x9b38e2d3bb358e1ceb8d7dd902585a53a5158844","status":0},"orignCredential":"test"},"context":"https://github.com/TencentCloud-Blockchain/TDID/blob/main/context/v1","CPTId":1,"expirationDate":1656487500,"id":"7c9c02bedace4a23be8885df6c4ead92","issuanceDate":1652410271,"issuer":"did:tdid:w1:0x9b38e2d3bb358e1ceb8d7dd902585a53a5158844","proof":{"created":1652410271,"creator":"did:tdid:w1:0x9b38e2d3bb358e1ceb8d7dd902585a53a5158844#keys-0","salt":{"action":"dton2","credentialStatus":{"credentialId":"LSJS0","issuer":"HLeve","status":"84HbY"},"orignCredential":"si5ML"},"signatureValue":"MEUCIFRUY/kghz/EhMmyEwbepfgyDS2o2dEjzvxO3hkU6Qi+AiEAkOnO5QV3Nl4NpyKUprioYvBJKAPvf7dFQO5QACoUq1I=","type":"Sm2p256v1"},"type":["VerifiableCredential","original","OperateCredential"]} \
    --PolicyJson {"orignCredential": 0, "action": 1, "credentialStatus": {"credentialId":1}}
```

Output: 
```
{
    "Response": {
        "CredentialData": "{\"claim\":{\"action\":\"SetCredentialStatus\",\"credentialStatus\":{\"credentialId\":\"0d8062f09bff4eb5b9697d1de28eebda\",\"issuer\":\"0xc3d893f67c506250ca69c355e4ee839b6c3199713249458a1248efbb948203dd\",\"status\":\"0x1b048d72a2479a229907d35c34ba69f8c65550daee1cb41cc1217d7e4a6850b9\"},\"orignCredential\":\"0xec55ac16ba42d6e2e9d4e6e7e78b3ca5a639cab555ed175c03b955b9dd109b53\"},\"context\":\"https://github.com/TencentCloud-Blockchain/TDID/blob/main/context/v1\",\"CPTId\":1,\"credentialType\":\"ORIGINAL\",\"expirationDate\":1656487500,\"hash\":\"0xfa21d5cc9b1c01d36801092177b341a4381ca2f07dae94e570e35f962c14b220\",\"id\":\"7c9c02bedace4a23be8885df6c4ead92\",\"issuanceDate\":1652410271,\"issuer\":\"did:tdid:w1:0x9b38e2d3bb358e1ceb8d7dd902585a53a5158844\",\"proof\":{\"created\":1652410271,\"creator\":\"did:tdid:w1:0x9b38e2d3bb358e1ceb8d7dd902585a53a5158844#keys-0\",\"salt\":{\"action\":\"dton2\",\"credentialStatus\":{\"credentialId\":\"LSJS0\",\"issuer\":\"0\",\"status\":\"0\"},\"orignCredential\":\"0\"},\"signatureValue\":\"MEUCIFRUY/kghz/EhMmyEwbepfgyDS2o2dEjzvxO3hkU6Qi+AiEAkOnO5QV3Nl4NpyKUprioYvBJKAPvf7dFQO5QACoUq1I=\",\"type\":\"Sm2p256v1\"},\"proofType\":\"Sm2p256v1\",\"type\":[\"VerifiableCredential\",\"original\",\"OperateCredential\"]}",
        "RequestId": "41a9acae-cef4-4949-b144-48c65ad5e425"
    }
}
```

