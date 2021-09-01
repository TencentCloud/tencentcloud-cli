**Example 1: 查询指定时间点是否看回档**



Input: 

```
tccli cynosdb DescribeRollbackTimeValidity --cli-unfold-argument  \
    --ClusterId cynosdbpg-gn65y9nk \
    --ExpectTime 2019-01-1302:12:05 \
    --ExpectTimeThresh 0
```

Output: 
```
{
    "Response": {
        "PoolId": 1050,
        "QueryId": 2008,
        "Status": "pass",
        "SuggestTime": ""
    }
}
```

