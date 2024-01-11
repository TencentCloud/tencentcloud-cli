**Example 1: 颁发可验证凭证**

凭证颁发方签发可验证凭证

Input: 

```
tccli tdid IssueCredential --cli-unfold-argument  \
    --DAPId 37 \
    --CRDLArg.CPTId 1 \
    --CRDLArg.Issuer did:tdid:w1:0x2e3455523646b1f4ebb40fe0c244bc329eb6fcbc \
    --CRDLArg.ExpirationDate 2023-06-29 15:25:00 \
    --CRDLArg.ClaimJson {"action": "deactiveDid","id": "did:tdid:w1:0x2e3455523646b1f4ebb40fe0c244bc329eb6fcbc","deactivated": "true", "__trans__": {"x": "a", "y": 1} }
```

Output: 
```
{
    "Response": {
        "RequestId": "41a9acae-cef4-4949-b144-48c65ad5e425",
        "CredentialData": "{\"CPTId\":1,\"issuer\":\"did:tdid:w1:0x2e3455523646b1f4ebb40fe0c244bc329eb6fcbc\",\"expirationDate\":\"2023-06-29T23:25:00+08:00\",\"issuanceDate\":\"2023-03-10T00:35:40+08:00\",\"context\":\"https://github.com/TencentCloud-Blockchain/TDID/blob/main/context/v1\",\"id\":\"88825f41be9648ddb292744ca6468db7\",\"type\":[\"VerifiableCredential\"],\"credentialSubject\":{\"action\":\"deactiveDid\",\"id\":\"did:tdid:w1:0x2e3455523646b1f4ebb40fe0c244bc329eb6fcbc\"},\"proof\":{\"created\":\"2023-03-10T00:35:40+08:00\",\"creator\":\"did:tdid:w1:0x2e3455523646b1f4ebb40fe0c244bc329eb6fcbc#keys-0\",\"signatureValue\":\"MEUCIQDcngP25ZCDNgZJI4zwyaRcKw2Mk99uvd32RDSjN0gZDAIgLSTslRrTet3Wi/lCgFtF4rmkjq5T8bBD4Cehmu5th1c=\",\"type\":\"Sm2p256v1\",\"txDegist\":\"8db419f0d1412340cfceb2ab28eff3d79615dc4d97ba67e58201a36eebc6e177\",\"vcDegist\":\"337bd77829fabf372eb8584b27bdbb3bb06610d70b2e64a96aff6f8a62116648\",\"method\":\"\",\"salt\":{\"action\":\"oY4YW\",\"id\":\"jxKzd\"}}}"
    }
}
```

