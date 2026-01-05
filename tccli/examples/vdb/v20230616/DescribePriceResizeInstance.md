**Example 1: 成功**



Input: 

```
tccli vdb DescribePriceResizeInstance --cli-unfold-argument  \
    --InstanceId vdb-8x28fw3t \
    --Cpu 4 \
    --Memory 16 \
    --DiskSize 50 \
    --WorkerNodeNum 3
```

Output: 
```
{
    "Response": {
        "Currency": "CNY",
        "OriginalPrice": 221100,
        "Price": 73260,
        "RequestId": "0d90bce5-2dfa-4837-9287-252d8afa55c9"
    }
}
```

