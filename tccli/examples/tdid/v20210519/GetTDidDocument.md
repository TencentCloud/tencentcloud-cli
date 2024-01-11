**Example 1: 获取DID标识的文档**

无

Input: 

```
tccli tdid GetTDidDocument --cli-unfold-argument  \
    --DAPId 1 \
    --Did did:tdid:w1:0x05cdde231b90dbcb1e0a9e7a616bf17c7168c2ac
```

Output: 
```
{
    "Response": {
        "Document": "{\n  \"@context\" : \"https://github.com/TencentCloud-Blockchain/TDID/blob/main/context/v1\",\n  \"symbol\" : \"BAYC\",\n  \"creator\" : \"did:tdid:w1:0x1a8ca5daffe98e48483fa58d7b352998c34705ca\",\n  \"controller\" : \"did:tdid:w1:0x6206a748ad9d3bc35fdbe6ac5248791ae9bb8d45\",\n  \"created\" : \"2022-08-08T03:23:40+0000\",\n  \"contract\" : \"BAYC1659929019\",\n  \"totalCount\" : 1,\n  \"deactivated\" : false,\n  \"versionId\" : 1,\n  \"baseUrl\" : \"https://ipfs.io/ipfs/QmeSjSinHpPnmXmspMjwiXyN6zS4E9zccariGR3jxcaWtq\",\n  \"service\" : [ ],\n  \"portalUrl\" : \"\",\n  \"name\" : \"BoredApeYachtClub\",\n  \"id\" : \"did:tdid:cm775g1:0x6206a748ad9d3bc35fdbe6ac5248791ae9bb8d45\",\n  \"verificationMethod\" : [ {\n    \"controller\" : \"did:tdid:cm775g1:0x6206a748ad9d3bc35fdbe6ac5248791ae9bb8d45\",\n    \"id\" : \"did:tdid:cm775g1:0x6206a748ad9d3bc35fdbe6ac5248791ae9bb8d45#keys-0\",\n    \"publicKey\" : \"-----BEGIN PUBLIC KEY-----\\r\\nMFkwEwYHKoZIzj0CAQYIKoEcz1UBgi0DQgAE8AxGIIZS5gNWEBmoAOsHxPd/8D2DrKqMuiWG2cVvYDt6H0CjWixP/RYeTXyRDjuLXd2tINL5VWKzm1EOlhQE+w==\\r\\n-----END PUBLIC KEY-----\",\n    \"type\" : \"Sm2p256v1\",\n    \"revoked\" : false\n  } ],\n  \"updated\" : \"2022-08-08T03:23:40+0000\",\n  \"desc\" : \"Bored Ape Yacht Club\",\n  \"authentication\" : [ \"#keys-0\" ]\n}",
        "RequestId": "fac6ef5a-7637-4a75-a2d3-0f7d87b5b8b5"
    }
}
```

