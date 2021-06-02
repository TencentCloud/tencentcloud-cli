**Example 1: 示例**

用户通过本接口向BTOE写入待存证的原文数据Hash值，BTOE对业务数据Hash值存证上链，并生成无电子签章的区块链存证电子凭证。

Input: 

```
tccli btoe CreateHashDepositNoSeal --cli-unfold-argument  \
    --BusinessId as1111323311 \
    --EvidenceInfo 业务扩展信息 \
    --EvidenceHash 数据hash
```

Output: 
```
{
    "Response": {
        "BusinessId": "as1111323311",
        "EvidenceId": "as1111323311",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

