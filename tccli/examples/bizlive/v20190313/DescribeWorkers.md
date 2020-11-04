**Example 1: DescribeWorkers示例**



Input: 

```
tccli bizlive DescribeWorkers --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Idle": 66,
        "RegionNum": 2,
        "RegionDetail": [
            {
                "region": "ap-gaungzhou",
                "idle": 31
            },
            {
                "region": "ap-shanghai",
                "idle": 35
            }
        ]
    },
    "RequestId": "7d95d7cd-2141-4ad6-a011-7ee116513407"
}
```

