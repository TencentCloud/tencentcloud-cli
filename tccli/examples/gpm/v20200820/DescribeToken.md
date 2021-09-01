**Example 1: 查询匹配Token示例**



Input: 

```
tccli gpm DescribeToken --cli-unfold-argument  \
    --MatchCode match-58mnuqlz
```

Output: 
```
{
    "Response": {
        "MatchToken": "mytoken",
        "CompatibleSpan": 180,
        "RequestId": "ab6ab15a-ab3a-495c-8818-e826084ea072"
    }
}
```

