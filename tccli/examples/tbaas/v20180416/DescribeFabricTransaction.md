**Example 1: DescribeFabricTransaction**

DescribeFabricTransaction

Input: 

```
tccli tbaas DescribeFabricTransaction --cli-unfold-argument  \
    --ClusterId fabric-65z42qi150 \
    --ChannelId channel-9xej4d \
    --TxId 03389f4a5af1883347ecdb15471e70abf3a8e6cf5b6648dc789674af7930e229
```

Output: 
```
{
    "Response": {
        "BlockHeight": 4,
        "ChaincodeName": "_lifecycle",
        "CreateTime": "2023-08-05 15:44:04",
        "JoinOrgList": [
            "org-xxxx.fabric-ian2bqtylk"
        ],
        "RequestId": "b5221353-8f20-4547-8260-c550b4b0175c",
        "Sender": "org-xxxx.fabric-ian2bqtylk",
        "TransactionData": "eyJjaGFpbmNvZGVfc3BlYyI6eyJjaGFpbmNvZGVfaWQiOnsibmFtZSI6Il9saWZlY3ljbGUiLCJwYXRoIjoiIiwidmVyc2lvbiI6IiJ9LCJpbnB1dCI6eyJhcmdzIjpbIkNvbW1pdENoYWluY29kZURlZmluaXRpb24iLCJcdTAwMDhcdTAwMDFcdTAwMTJcdTAwMDNteWNcdTAwMWFcdTAwMDR2MS4wXCJcdTAwMDRlc2NjKlx1MDAwNHZzY2MyMVxuL1x1MDAxMlx1MDAwOFx1MDAxMlx1MDAwNlx1MDAwOFx1MDAwMVx1MDAxMlx1MDAwMlx1MDAwOFx1MDAwMFx1MDAxYSNcdTAwMTIhXG5cdTAwMWZvcmctMjUxMDA1NzQ2LmZhYnJpYy02NXo0MnFpMTUwOlx1MDAwMCJdLCJkZWNvcmF0aW9ucyI6e30sImlzX2luaXQiOmZhbHNlfSwidGltZW91dCI6MCwidHlwZSI6IlVOREVGSU5FRCJ9fQ==",
        "TxHash": "8e5b978d33cfbc0510b4e60406f8481f8ec00e390131d5b6ea6d38604e1bcb46",
        "TxId": "03389f4a5af1883347ecdb15471e70abf3a8e6cf5b6648dc789674af7930e229",
        "TxStatus": "VALID"
    }
}
```

