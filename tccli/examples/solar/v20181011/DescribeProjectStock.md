**Example 1: DescribeProjectStock**



Input: 

```
tccli solar DescribeProjectStock --cli-unfold-argument  \
    --SubProjectId subprj-7df8mxtutd
```

Output: 
```
{
    "Response": {
        "ProjectStocks": [
            {
                "PoolIdx": 1,
                "PoolName": "奖池1",
                "PrizeBat": 1,
                "PrizeId": "res-7p4ohdtip7",
                "PrizeName": "test",
                "RemainStock": 1100,
                "UsedStock": 1
            }
        ],
        "RequestId": "ed458170-a473-4b81-a0e3-856d6b364c19"
    }
}
```

