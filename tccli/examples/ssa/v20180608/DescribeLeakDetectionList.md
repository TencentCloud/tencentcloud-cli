**Example 1: 获取泄露列表**



Input: 

```
tccli ssa DescribeLeakDetectionList --cli-unfold-argument  \
    --Limit 10 \
    --Page 1 \
    --StartTime YYYY-MM-DD \
    --EndTime YYYY-MM-DD
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "List": [
            "name"
        ],
        "RequestId": "1ba104fc-e008-4f70-8d45-e72199004fa7"
    }
}
```

