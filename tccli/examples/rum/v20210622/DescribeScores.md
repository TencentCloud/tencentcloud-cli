**Example 1: 获取首页Score**

获取首页Score

Input: 

```
tccli rum DescribeScores --cli-unfold-argument  \
    --ID 1 \
    --StartTime 2020011920 \
    --EndTime 2022051914
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

**Example 2: 12**



Input: 

```
tccli rum DescribeScores --cli-unfold-argument  \
    --EndTime 2021012611 \
    --ID 1 \
    --StartTime 2021012111
```

Output: 
```
null
```

