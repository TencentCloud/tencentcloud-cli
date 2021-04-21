**Example 1: 哈希存证测试示例**



Input: 

```
tccli btoe CreateHashDeposit --cli-unfold-argument  \
    --HashType 0 \
    --EvidenceDescription 哈希存证 \
    --BusinessId 5671ad9c-ebaa-4d96-a2bc-0fcb71b36f2b \
    --EvidenceName 哈希存证测试 \
    --EvidenceHash ce98712408c9fc580be2ff208efeb6c154530ca2b968c2b41af3bbd4b3eab7ec
```

Output: 
```
{
    "Response": {
        "RequestId": "15d49052-b85b-4418-a2e4-fa4f6a882a0f",
        "EvidenceId": "15d49052-b85b-4418-a2e4-fa4f6a882a0f",
        "BusinessId": "5671ad9c-ebaa-4d96-a2bc-0fcb71b36f2b"
    }
}
```

