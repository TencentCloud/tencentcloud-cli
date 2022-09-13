**Example 1: 升级预付费存储**



Input: 

```
tccli cynosdb ModifyClusterStorage --cli-unfold-argument  \
    --ClusterId cynosdbmysql-xxxxxxxx \
    --NewStorageLimit 20 \
    --OldStorageLimit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "132075",
        "TranId": "20190522160000003106844584180998",
        "BigDealIds": [
            "xxx"
        ],
        "DealNames": [
            "20190522112283"
        ]
    }
}
```

