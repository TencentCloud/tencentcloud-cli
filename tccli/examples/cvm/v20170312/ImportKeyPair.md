**Example 1: Importing a key pair**



Input: 

```
tccli cvm ImportKeyPair --cli-unfold-argument  \
    --KeyName operation_key\
    --ProjectId 0\
    --PublicKey 'ssh-rsa XXXXXXXXXXXX'
```

Output: 
```
{
    "Response": {
        "KeyId": "skey-4e5ty7i8",
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

