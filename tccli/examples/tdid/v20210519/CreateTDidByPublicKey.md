**Example 1: CreateTDidByPublicKey**

根据公私钥生成Tdid

Input: 

```
tccli tdid CreateTDidByPublicKey --cli-unfold-argument  \
    --ClusterId bcos-fmtkyt8xne \
    --GroupId 1 \
    --PublicKey 7430488790716037455843285301209475352340487000630103610741044889217493578632422416688836099438173061252937088504002356479929639821721792771207629422355422 \
    --EncryptPubKey 7430488790716037455843285301209475352340487000630103610741044889217493578632422416688836099438173061252937088504002356479929639821721792771207629422355422
```

Output: 
```
{
    "Response": {
        "Did": "did:tdid:1:0x4b5edc27dd8a20ebaae6d427f3142b24fbf687ff",
        "RequestId": "41a9acae-cef4-4949-b144-48c65ad5e425"
    }
}
```
