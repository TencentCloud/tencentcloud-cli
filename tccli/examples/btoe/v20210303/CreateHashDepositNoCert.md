**Example 1: 哈希上链存证**

用户通过本接口向BTOE写入待存证的原文数据Hash值，BTOE对业务数据Hash值存证上链。

Input: 

```
tccli btoe CreateHashDepositNoCert --cli-unfold-argument  \
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

**Example 2: 示例**



Input: 

```
tccli btoe CreateHashDepositNoCert --cli-unfold-argument  \
    --HashType 0 \
    --EvidenceInfo 34545 \
    --BusinessId 777 \
    --EvidenceHash 34543
```

Output: 
```
{
    "Response": {
        "RequestId": "f3fe7162-b32f-469b-9850-3e3e328dfec5",
        "BusinessId": "777",
        "EvidenceId": "f3fe7162-b32f-469b-9850-3e3e328dfec5",
        "EvidenceTime": "2021-04-08 17:44:10",
        "EvidenceTxHash": "0xf80ee164f4ef86d285d9eab166773700f27d1ac3f124df2fa62f482b743d8a05",
        "BlockchainHeight": 3354
    }
}
```

