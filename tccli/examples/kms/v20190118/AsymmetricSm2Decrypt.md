**Example 1: 非对称密钥Sm2解密**



Input: 

```
tccli kms AsymmetricSm2Decrypt --cli-unfold-argument  \
    --KeyId 554ef4b3-3071-11ea-a86a-5254006d0810 \
    --Ciphertext Fb0UICocErQgNEkYKJagtoKNed7DLeo5UkZzPJMyI94CfWh6yKHGgb/0PBHrCve2Avo4gJI5pJMWP3Aq5ggX0aunLv87UX+sgO1/3HXW+q4ARaiwZ9Q73RQuPg6qJ2Eg33uZ2Xjey3l+5yHiOdZYmCVePtKAsuhxzKw/sALTbGTYYnbJXnGKr3Yu7Hs0hCC1bOz0sNqd1IXdUyMtQtbDOV8NWg2ecdZPIOdbnrCKIQ4rpMUghjSFv3rSHo5VbpuOGPXqEZT4goou42psIXb03li3TXxFZMTAdxVMzpqEuTfRxiMPEqyPEHe6xG92vJX0FZfWU8Y5SxlfXp+mvBbAmw
```

Output: 
```
{
    "Response": {
        "RequestId": "7c076c83-1402-41d8-8ce6-73a350a9eaf6",
        "KeyId": "554ef4b3-3071-11ea-a86a-5254006d0810",
        "Plaintext": "dGVzdA=="
    }
}
```

