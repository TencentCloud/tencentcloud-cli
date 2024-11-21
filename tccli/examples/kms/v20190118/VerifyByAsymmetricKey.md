**Example 1: 使用非对称密钥验签**



Input: 

```
tccli kms VerifyByAsymmetricKey --cli-unfold-argument  \
    --KeyId d79e97e5-69d1-11ef-bc87-02ac442a5a1f \
    --SignatureValue MEUCIQDunw5PZuSVI6IPX2xxdce6ohrm9Rt8KBqpMr6yogDbdgIgVyqCOiOs9OVb/frwglpg+43QXMMRnFKmBd5VNpS4A/o= \
    --Message dGVzdAo= \
    --MessageType RAW \
    --Algorithm SM2DSA
```

Output: 
```
{
    "Response": {
        "RequestId": "020b75ba-22f8-4f53-ab16-46ae5120711a",
        "SignatureValid": true
    }
}
```

