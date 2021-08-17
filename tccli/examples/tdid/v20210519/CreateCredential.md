**Example 1: CreateCredential**

创建凭证

Input: 

```
tccli tdid CreateCredential --cli-unfold-argument  \
    --TransactionArg.InvokerTDid did:tdid:15:0xbd7345b2ff8d1dbf1e330a6c5dcf20c675b6c484 \
    --VersionCredential 1.0.0 \
    --FunctionArg.ClaimJson {"name": "zhang san", "id": "did:tdid:15:0x3b67623cbdaa9ccbfc8b7c346588c6bcbc6f5d63", "age": 18} \
    --FunctionArg.ExpirationDate 2029-04-18T21:12:33Z \
    --FunctionArg.CptId 2000000 \
    --FunctionArg.Issuer did:tdid:15:0xbd7345b2ff8d1dbf1e330a6c5dcf20c675b6c484
```

Output: 
```
{
    "Response": {
        "CredentialData": "{\"claim\":{\"age\":18,\"id\":\"did:tdid:15:0x3b67623cbdaa9ccbfc8b7c346588c6bcbc6f5d63\",\"name\":\"zhang san\"},\"context\":\"https://github.com/WeBankFinTech/WeIdentity/blob/master/context/v1\",\"cptId\":2000000,\"expirationDate\":1871212353,\"id\":\"0a581276-35e8-4835-ae5d-66705c76335d\",\"issuanceDate\":1628136106,\"issuer\":\"did:tdid:15:0xbd7345b2ff8d1dbf1e330a6c5dcf20c675b6c484\",\"proof\":{\"created\":1628136106,\"creator\":\"did:tdid:15:0xbd7345b2ff8d1dbf1e330a6c5dcf20c675b6c484#keys-0\",\"salt\":{\"age\":\"APoZk\",\"id\":\"LxxnG\",\"name\":\"9upnW\"},\"signatureValue\":\"3qFEuH8Oa7oVWEBSRHSG/iHYVqmTFtnQH+bES3UQTuYYw9m82hP87cDf4s2P5C+h5/I7UqsEJzXz1KRBklrhpAA=\",\"type\":\"Secp256k1\"},\"type\":[\"VerifiableCredential\",\"original\"]}",
        "RequestId": "41a9acae-cef4-4949-b144-48c65ad5e425"
    }
}
```

