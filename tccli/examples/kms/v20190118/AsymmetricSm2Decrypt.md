**Example 1: 非对称密钥Sm2解密**



Input: 

```
tccli kms AsymmetricSm2Decrypt --cli-unfold-argument  \
    --KeyId fce1015e-9735-11ef-be86-6abd61583d2d \
    --Ciphertext MG0CICuRefoqE7g5bpsZNYq+9d909cZl7nFuYFHiDhOqz8GAAiEA4lqmt3nGqpbu0qhbWsStkexXA2cA12nVWjgruFP5WKkEIG6JwYejm9gEr7CPOOhbirsGhga3W7J6C7kwdmf6VebRBATH1o2G
```

Output: 
```
{
    "Response": {
        "KeyId": "fce1015e-9735-11ef-be86-6abd61583d2d",
        "Plaintext": "dGVzdA==",
        "RequestId": "e2e0945e-7e90-421a-bfc8-64999d789283"
    }
}
```

