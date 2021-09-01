**Example 1: 解密接口示例**

用于对密文解密

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

