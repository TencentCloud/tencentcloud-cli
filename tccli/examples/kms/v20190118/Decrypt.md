**Example 1: Decrypting**

This example shows you how to decrypt the ciphertext.

Input: 

```
tccli kms Decrypt --cli-unfold-argument  \
    --CiphertextBlob Ade234dasdeEWdGVzdCUyMHBsYWlJJlIHL
```

Output: 
```
{
    "Response": {
        "KeyId": "23e80852-1e38-11e9-b129-5cb9019b4b01",
        "Plaintext": "dGVzdCUyMHBsYWluJTIwdGV4dA==",
        "RequestId": "1b580852-1e38-11e9-b129-5cb9019b4b00"
    }
}
```

