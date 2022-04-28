**Example 1: CreateSelectiveCredential**

生成选择性批露凭证

Input: 

```
tccli tdid CreateSelectiveCredential --cli-unfold-argument  \
    --FunctionArg.Type VerifiableCredential original \
    --FunctionArg.Context https://github.com/WeBankFinTech/WeIdentity/blob/master/context/v1 \
    --FunctionArg.ClaimJson {"name": "zhang san", "id": "did:tdid:15:0x3b67623cbdaa9ccbfc8b7c346588c6bcbc6f5d63", "age": 18} \
    --FunctionArg.CptId 2000000 \
    --FunctionArg.ExpirationDate 1871212353 \
    --FunctionArg.Id 657b9ea7-99d3-4068-9c2b-fe1593929474 \
    --FunctionArg.IssuanceDate 1628588966 \
    --FunctionArg.Issuer did:tdid:cb591-1:0x0e6c51028750e90815bbb3968fbb58c1c9fe8e08 \
    --FunctionArg.Proof.Created 1628588966 \
    --FunctionArg.Proof.Creator did:tdid:cb591-1:0x0e6c51028750e90815bbb3968fbb58c1c9fe8e08#keys-0 \
    --FunctionArg.Proof.SignatureValue KhaMad6Y80VqKRFUH++j7odpEQwtlhCJhiON8lvo+fd9XJF9yV9skrd5khNSGcFSI8hibZpJvkN+Lp4tVG10nwA= \
    --FunctionArg.Proof.Type Secp256k1 \
    --FunctionArg.Proof.SaltJson {"age":"bTPhh","id":"sSPRi","name":"GB5uR"} \
    --PolicyId 2000014
```

Output: 
```
{
    "Response": {
        "CredentialData": "{\"claim\":{\"age\":\"0xa5082cabd3bba770fb2fb8fd75ecd660de978b4ddfa78ad9eeca2758acdf74d3\",\"id\":\"did:tdid:15:0x3b67623cbdaa9ccbfc8b7c346588c6bcbc6f5d63\",\"name\":\"zhang san\"},\"context\":\"https://github.com/WeBankFinTech/WeIdentity/blob/master/context/v1\",\"cptId\":2000000,\"credentialType\":\"ORIGINAL\",\"expirationDate\":1871212353,\"hash\":\"0x737480f2e94f32b957223365c84b991ab578a677dfefdee73fe1640cc614d443\",\"id\":\"657b9ea7-99d3-4068-9c2b-fe1593929474\",\"issuanceDate\":1628588966,\"issuer\":\"did:tdid:cb591-1:0x0e6c51028750e90815bbb3968fbb58c1c9fe8e08\",\"proof\":{\"created\":1628588966,\"creator\":\"did:tdid:cb591-1:0x0e6c51028750e90815bbb3968fbb58c1c9fe8e08#keys-0\",\"salt\":{\"age\":\"0\",\"id\":\"sSPRi\",\"name\":\"GB5uR\"},\"signatureValue\":\"KhaMad6Y80VqKRFUH++j7odpEQwtlhCJhiON8lvo+fd9XJF9yV9skrd5khNSGcFSI8hibZpJvkN+Lp4tVG10nwA=\",\"type\":\"Secp256k1\"},\"proofType\":\"Secp256k1\",\"salt\":{\"age\":\"0\",\"id\":\"sSPRi\",\"name\":\"GB5uR\"},\"signature\":\"KhaMad6Y80VqKRFUH++j7odpEQwtlhCJhiON8lvo+fd9XJF9yV9skrd5khNSGcFSI8hibZpJvkN+Lp4tVG10nwA=\",\"type\":[\"VerifiableCredential\",\"original\"]}",
        "RequestId": "41a9acae-cef4-4949-b144-48c65ad5e425"
    }
}
```

