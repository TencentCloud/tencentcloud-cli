**Example 1: CreateTDidByPrivateKey**

新建DID

Input: 

```
tccli tdid CreateTDidByPrivateKey --cli-unfold-argument  \
    --ClusterId bcos-fmtkyt8xne \
    --GroupId 1 \
    --PrivateKey 29331392255431342347427142407956379150860712035024674919338433021732260496669
```

Output: 
```
{
    "Response": {
        "Did": "did:tdid:1:0x6dcc17846844ff22046a3cc5ae51941defe0d02c",
        "RequestId": "41a9acae-cef4-4949-b144-48c65ad5e425"
    }
}
```

