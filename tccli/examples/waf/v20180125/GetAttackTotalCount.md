**Example 1: 攻击总次数**



Input: 

```
tccli waf GetAttackTotalCount --cli-unfold-argument  \
    --StartTime 2020-09-22T00:00:00+00:00 \
    --EndTime 2020-09-22T00:00:00+00:00 \
    --Domain waf.com \
    --QueryString bot:1
```

Output: 
```
{
    "Response": {
        "TotalCount": 271652,
        "RequestId": "9b02bf9e-c89c-42c3-9ae1-685f968fa02d"
    }
}
```

