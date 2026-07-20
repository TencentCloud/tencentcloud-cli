**Example 1: 拉取202060715日生成的种子密钥**



Input: 

```
tccli sts ListCosSessionSeedToken --cli-unfold-argument  \
    --Date 20260715 \
    --NextToken MTQ1MDA= \
    --Limit 500
```

Output: 
```
{
    "Response": {
        "Date": "20260715",
        "MatchExpected": 0,
        "NextToken": "",
        "SeedCredentials": [
            {
                "ExpireTime": 1784692801,
                "SeedSecretId": "8dM0nIabTc5XA6jxaHbyDqkdzc8UQNQa",
                "SeedSecretKey": "x0bWfT7oYj8vFus4iliLJKs9CwHokO8o",
                "SeedToken": "ek7HNy5g4ZRs9p6bvl3fYm4nukrzUkm5"
            }
        ],
        "RequestId": "e4bf2325-d123-40bd-b501-0f4dffb91abb"
    }
}
```

