**Example 1: 哈希上链存证**

用户通过本接口向BTOE写入待存证的原文数据Hash值，BTOE对业务数据Hash值存证上链。

Input: 

```
tccli btoe CreateHashDepositNoSeal --cli-unfold-argument  \
    --BusinessId as1111323311 \
    --EvidenceInfo 业务扩展信息 \
    --EvidenceHash 数据hash \
    --HashType 0
```

Output: 
```
{
    "Response": {
        "BusinessId": "as1111323311",
        "EvidenceId": "as1111323311",
        "EvidenceTime": "2021-04-07 14:22:20",
        "EvidenceTxHash": "数据hash",
        "BlockchainHeight": 800,
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

