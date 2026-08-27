**Example 1: 通过加密请求体进行请求**



Input: 

```
tccli ess CreateRequestWithEncryption --cli-unfold-argument  \
    --RequestAction DescribeFlowComponents \
    --IV ZeuAMEj5nEGZUtekyKqxKw== \
    --EncryptedData v7vwDVtF+ftVANPClwZxrCCKM1dgOq+X5rCDGdlNqwQ6wRzndA8QxLc7YA+txKeU92cqTdtuji3e+Il+uVJ0qQ4fnVM/A5WmLEp6adq7+iW7LxHc9qo72suf630bdYHrA9iuzr0nqUd05ronubzSFQ== \
    --EncryptionSignature uSnCx/PE/CTlckq5tZ+xqJMC2dd5Bg8Zg/ATSK0apkI=
```

Output: 
```
{
    "Response": {
        "EncryptedData": "60m8IgrRfRDWarWGd1KngYXdG0zYRNAv29iRMsR333F4nNoZhQvhXZo61DbUcm8YlEUfdLhDjK9f9fRXMr+ARH+3vOI/3k+owr3IYJAQeQ4p0zky95j8znlae3JBOwm06P/ED+dU90s9tb8pM3n0S06TpAxBZxryVmPpnqFyuDlbt9W5eb1KVz56WbPTp4QyjKWksc6tezquKe9FLx8u/x1/ZzHaunur2+StM2KkSZ8=",
        "EncryptionSignature": "z2aKvBr/WkSXWKwpu0LX2V1S2ZGP9K3LLP1hEfhJOWM=",
        "IV": "z/p4htlS/UwLpHwxHbyrFw==",
        "RequestId": "bde98308-b4b9-49c1-b46b-51d1d55d41da"
    }
}
```

