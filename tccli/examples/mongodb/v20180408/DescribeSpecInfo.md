**Example 1: 查询云数据库售卖**



Input: 

```
tccli mongodb DescribeSpecInfo --cli-unfold-argument  \
    --Region ap-guangzhou
```

Output: 
```
{
    "Response": {
        "RequestId": "a8c7ade4-2d22-4f5e-9e71-f546f15e6d67",
        "SpecInfoList": [
            {
                "Region": "ap-guangzhou",
                "Zone": "ap-guangzhou-3"
            }
        ]
    }
}
```

