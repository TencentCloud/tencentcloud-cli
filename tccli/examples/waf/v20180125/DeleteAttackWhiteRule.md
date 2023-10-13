**Example 1: 查询示例**



Input: 

```
tccli waf DeleteAttackWhiteRule --cli-unfold-argument  \
    --Domain xx \
    --Ids 1 2
```

Output: 
```
{
    "Response": {
        "FailIds": [
            1,
            2
        ],
        "RequestId": "xx"
    }
}
```

