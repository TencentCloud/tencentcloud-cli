**Example 1: 查询智能导诊订单列表**



Input: 

```
tccli ig DescribeIgOrderList --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 10 \
    --ProductType ig \
    --KeyWord 20210521001000429685321 \
    --OrderStatus 1
```

Output: 
```
{
    "Response": {
        "RequestId": "bea70601-4f99-4462-86ef-cddaae67bca0"
    }
}
```

