**Example 1: 查询用户列表**



Input: 

```
tccli ckafka DescribeAppInfo --cli-unfold-argument  \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 11,
            "AppIdList": [
                1251000011,
                1255426940,
                251000873,
                251000691,
                251006545,
                1251762227,
                1256134262,
                251006131,
                1251006288,
                1251006373
            ]
        },
        "RequestId": "8d7551b2-651e-4f47-80bc-13a478fda732"
    }
}
```

