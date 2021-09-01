**Example 1: 分页查询匹配code**



Input: 

```
tccli gpm DescribeMatchCodes --cli-unfold-argument  \
    --Offset 1 \
    --Limit 15 \
    --MatchCode match-rzsfvf
```

Output: 
```
{
    "Response": {
        "MatchCodes": [
            "match-rzsfvf"
        ],
        "RequestId": "eefe26e0-fc8a-41e4-a9be-69694662c6cc",
        "TotalCount": 0
    }
}
```

