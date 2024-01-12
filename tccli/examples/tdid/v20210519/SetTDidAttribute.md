**Example 1: 设置DID的自定义属性**

设置DID的自定义属性

Input: 

```
tccli tdid SetTDidAttribute --cli-unfold-argument  \
    --Did did:tdid:w1:0x0d342759f20005df531c50f671d414661e381c01 \
    --Attributes.0.Key test \
    --Attributes.0.Val test \
    --DAPId 5
```

Output: 
```
{
    "Response": {
        "RequestId": "0f7de9d2-2a60-46b1-97c3-62331ddf12ec",
        "Transaction": {
            "TransactionHash": "17864b02e92bea49ca4707214f59ac99910fecf8bfa8434380bb62471a09e61a"
        }
    }
}
```

