**Example 1: 获取首页Score**

获取首页Score

Input: 

```
tccli rum DescribeScores --cli-unfold-argument  \
    --EndTime 2022051914 \
    --ID 1 \
    --StartTime 2020011920
```

Output: 
```
{
    "Response": {
        "ScoreSet": [],
        "RequestId": "65a8fec7-2b39-4b11-893f-3715279d235f"
    }
}
```

