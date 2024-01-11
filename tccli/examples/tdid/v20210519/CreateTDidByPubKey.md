**Example 1: 导入公钥注册DID标识**

上传用户本地公钥文件创建DID标识

Input: 

```
tccli tdid CreateTDidByPubKey --cli-unfold-argument  \
    --DAPId 1 \
    --PublicKey -----BEGIN PUBLIC KEY-----
MFkwEwYHKoZIzj0CAQYIKoEcz1UBgi0DQgAEaI9IwGTO3SL6tamGNdyFi+zg8W7W
53dKNBC3xuRXdlbor0gTIlYSgKIyClY6KUrizmW6gMfKcrzBojml5j4JJg==
-----END PUBLIC KEY-----
```

Output: 
```
{
    "Response": {
        "RequestId": "fac6ef5a-7637-4a75-a2d3-0f7d87b5b8b5",
        "Did": "did:tdid:w1:0xdab41eb32082044366f1b5712504d0b623b095c1",
        "Transaction": {
            "TransactionHash": "1747ae57db16f1d6cac4b711742904f87030f3eee8704439aa203a8278d219c3"
        }
    }
}
```

