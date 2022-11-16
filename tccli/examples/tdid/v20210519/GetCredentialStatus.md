**Example 1: CreateLabel**

新建标签

Input: 

```
tccli tdid GetCredentialStatus --cli-unfold-argument  \
    --CredentialId 0a581276-35e8-4835-ae5d-66705c76335d
```

Output: 
```
{
    "Response": {
        "CredentialStatus": {
            "CredentialId": "0a581276-35e8-4835-ae5d-66705c76335d",
            "Status": 1,
            "Issuer": "did:tdid:15:0xbd7345b2ff8d1dbf1e330a6c5dcf20c675b6c484",
            "Digest": "XXXXXXXXXXXXXXXXXX",
            "Signature": "XXXXXXXXXXXXXXXXXX",
            "TimeStamp": 1645670370
        },
        "RequestId": "41a9acae-cef4-4949-b144-48c65ad5e425"
    }
}
```

