**Example 1: 非对称密钥签名**



Input: 

```
tccli kms SignByAsymmetricKey --cli-unfold-argument  \
    --Algorithm SM2DSA \
    --Message dGVzdAo= \
    --KeyId d79e97e5-69d1-11ef-bc87-02ac442a5a1f \
    --MessageType RAW
```

Output: 
```
{
    "Response": {
        "RequestId": "f60b4087-ab02-4c5b-bf50-956e591ccbc4",
        "Signature": "MEYCIQDFunV6ujrE9k4IMOEeH4J0uwENYSf1JH2DI01qlFWKkwIhAMiv6S2s3VsLtMF/+4rDEiF3IyE3zfRGq5B+k7hHfGoQ"
    }
}
```

