**Example 1: 新建企业订单**



Input: 

```
tccli trp CreateCorporationOrder --cli-unfold-argument  \
    --CodeQuota 10000 \
    --CorpId 1000 \
    --Amount 10000 \
    --ContactPerson 张三 \
    --ExpireTime 2023-12-31 23:59:59 \
    --ContactNumber 13912345678 \
    --Owner 1000 \
    --CorpName 张三企业 \
    --Remark 张三
```

Output: 
```
{
    "Response": {
        "CorpId": 1,
        "RequestId": "xx"
    }
}
```

