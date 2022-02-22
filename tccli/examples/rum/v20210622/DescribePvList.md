**Example 1: 获取PV列表**



Input: 

```
tccli rum DescribePvList --cli-unfold-argument  \
    --ProjectId 1 \
    --StartTime "1" \
    --EndTime "20" \
    --Dimension "d"
```

Output: 
```
{
    "Response": {
        "ProjectPvSet": [],
        "RequestId": "65a8fec7-2b39-4b11-893f-3715279d235f"
    }
}
```

