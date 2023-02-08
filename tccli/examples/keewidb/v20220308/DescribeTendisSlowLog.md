**Example 1: 示例1**



Input: 

```
tccli keewidb DescribeTendisSlowLog --cli-unfold-argument  \
    --InstanceId kee-9clkb977 \
    --Offset 0 \
    --Limit 100 \
    --BeginTime 2022-03-10 13:22:03 \
    --MinQueryTime 10 \
    --EndTime 2022-03-10 14:22:03
```

Output: 
```
{
    "Response": {
        "RequestId": "e7018395-c189-4b73-9d3c-eec3c3b2b9e6",
        "TendisSlowLogDetail": [],
        "TotalCount": 0
    }
}
```

