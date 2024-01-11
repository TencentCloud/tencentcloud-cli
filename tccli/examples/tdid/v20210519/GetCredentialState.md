**Example 1: 获取凭证链上状态信息**

获取凭证链上状态信息

Input: 

```
tccli tdid GetCredentialState --cli-unfold-argument  \
    --CredentialId 8818fdd61eb84e4a745a3b04c96e5237 \
    --DAPId 5
```

Output: 
```
{
    "Response": {
        "RequestId": "10f21d53-43f7-4736-a028-384b446132d0",
        "CredentialState": {
            "Id": "8818fdd61eb84e4a745a3b04c96e5237",
            "Status": 1,
            "CPTId": 1,
            "Issuer": "did:tdid:c5:0xe0fd109747937fbaf68ef1f615c2cd8e87d22ffb",
            "TXDigest": "",
            "VCDigest": "c7e13c5bcfa879c922f9141d085facc0ce1973e8d27d48238130739c1a332dcf",
            "MetaDigest": "6a216f84cb9c5b6170cb017cccd6c5d0b81aad200d5691914d6045471d0dd1ad",
            "IssueTime": 1695125060,
            "ExpireTime": 1701396000,
            "Signature": "MEUCIQDUneIwlLbh5AFjQt9HJhIZAQshT45/Em8hVOUjHcdu0QIgL3rg3A99qGGNszstF+GTV5IU4vT9OnI1lqM3f0c5JmI="
        }
    }
}
```

