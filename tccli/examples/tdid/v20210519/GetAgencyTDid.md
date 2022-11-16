**Example 1: 本机构DID详情**



Input: 

```
tccli tdid GetAgencyTDid --cli-unfold-argument  \
    --ClusterId bcos-fmtkyt8xne
```

Output: 
```
{
    "Response": {
        "Prefix": "did:tdid:",
        "Identity": [
            {
                "AccountIdentifier": "0x3c4d1e80a1bb5a2558b50ca4b76b85c88bfbf472",
                "ChainID": "15",
                "Did": "did:tdid:1:0x3c4d1e80a1bb5a2558b50ca4b76b85c88bfbf472"
            }
        ],
        "RequestId": "41a9acae-cef4-4949-b144-48c65ad5e425"
    }
}
```

