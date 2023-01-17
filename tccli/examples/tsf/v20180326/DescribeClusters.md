**Example 1: 获取集群列表示例**



Input: 

```
tccli tsf DescribeClusters --cli-unfold-argument  \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "6d7e580e-4b1c-49a7-8ffd-21551f865643",
        "Result": {
            "TotalCount": 0,
            "Content": []
        }
    }
}
```

