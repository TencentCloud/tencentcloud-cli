**Example 1: SetCredentialStatus**

新建标签

Input: 

```
tccli tdid SetCredentialStatus --cli-unfold-argument  \
    --CredentialStatus.CredentialId 0a581276-35e8-4835-ae5d-66705c76335d \
    --CredentialStatus.Status 1 \
    --CredentialStatus.Issuer did:tdid:15:0xbd7345b2ff8d1dbf1e330a6c5dcf20c675b6c484 \
    --CredentialStatus.Digest XXXXXXXXXXXXXXXXXX \
    --CredentialStatus.Signature XXXXXXXXXXXXXXXXXX \
    --CredentialStatus.TimeStamp 1645670370
```

Output: 
```
{
    "Response": {
        "RequestId": "41a9acae-cef4-4949-b144-48c65ad5e425"
    }
}
```

