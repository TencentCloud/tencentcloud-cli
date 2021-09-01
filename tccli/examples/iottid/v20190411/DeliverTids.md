**Example 1: 空发TID**



Input: 

```
tccli iottid DeliverTids --cli-unfold-argument  \
    --OrderId SbRTDKP1L4 \
    --Quantity 1
```

Output: 
```
{
    "Response": {
        "ProductKey": "432hfbb4324132etgzsdbgfxhg14344gfdsgbgfrrttgrhgfcgh251bd08aa58f048591087c7f551292eb6da1d56ffb0d32bc81fa97b92f1d42b138099f97fd676d0680357b9cb5a4",
        "RequestId": "96a3691c-25ff-471b-94c2-48526757510e",
        "TidSet": [
            {
                "PrivateKey": "1c09446f8ebc03b3b3b148f9c236e221768ccd2e1df24ec6fd02db26043f576a",
                "Psk": "4a802bbe514395496b93a4dd9776af0352c060290f504396b8357ae9d571a5f3",
                "PublicKey": "99a7bcac2cb6f4e94e1d4e4c23fb940dfddb251bd08aa58f048591087c7f551292eb6da1d56ffb0d32bc81fa97b92f1d42b138099f97fd676d0680357b9cb5a4",
                "Tid": "010001015D0C939457E5860182C4FC14"
            }
        ]
    }
}
```

