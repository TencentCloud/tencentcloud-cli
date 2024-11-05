**Example 1: 查询示例**



Input: 

```
tccli waf DeleteAttackWhiteRule --cli-unfold-argument  \
    --Domain www.test.com \
    --Ids 1 2
```

Output: 
```
{
    "Response": {
        "FailIds": [
            1
        ],
        "RequestId": "1cc54bf4-cfeb-40cc-a823-035e52106df9"
    }
}
```

