**Example 1: 查询新购分布式数据库实例的价格（示例中返回价格仅供参考）**



Input: 

```
tccli dcdb DescribeDCDBPrice --cli-unfold-argument  \
    --ShardMemory 2 \
    --ShardStorage 10 \
    --ShardNodeCount 3 \
    --ShardCount 2 \
    --Zone ap-guangzhou-2 \
    --Count 1 \
    --Period 1
```

Output: 
```
{
    "Response": {
        "RequestId": "7e1000c2-190a-d0df-ff75-59fbdf5ff381",
        "OriginalPrice": 42240,
        "Price": 42240
    }
}
```

