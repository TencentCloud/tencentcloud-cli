**Example 1: 查询示例**



Input: 

```
tccli waf DeleteAttackWhiteRule --cli-unfold-argument  \
    --Domain  \
    --Ids 1 2
```

Output: 
```
{
    "Response": {
        "FailIds": [
            1
        ],
        "RequestId": "abc"
    }
}
```

