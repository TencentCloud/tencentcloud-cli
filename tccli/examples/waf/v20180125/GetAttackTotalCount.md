**Example 1: 攻击总次数**



Input: 

```
tccli waf GetAttackTotalCount --cli-unfold-argument  \
    --StartTime 2021-02-01T00:00:00+08:00 \
    --EndTime 2021-02-25T23:59:59+08:00 \
    --Domain xxx \
    --QueryString yyy
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

