**Example 1: 自动生成公私钥注册DID**

TDID平台自动生成公私钥对托管在DID平台，并注册DID

Input: 

```
tccli tdid CreateTDidByHost --cli-unfold-argument  \
    --DAPId 1 \
    --CustomAttribute {"a":{"c":1},"b":"test"}
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

