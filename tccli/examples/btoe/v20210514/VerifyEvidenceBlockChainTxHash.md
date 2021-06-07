**Example 1: BTOE区块链交易hash核验**

用户向BTOE核验存证结果中的区块链交易hash，核验成功后会返回存证信息

Input: 

```
tccli btoe VerifyEvidenceBlockChainTxHash --cli-unfold-argument  \
    --EvidenceTxHash 区块链交易Hash
```

Output: 
```
{
    "Response": {
        "RequestId": "121212",
        "EvidenceTime": "2021-03-31 18:52:05",
        "EvidenceId": "005ff9c5-1891-a546-3c4d-cdaee32050a3",
        "Result": true
    }
}
```

