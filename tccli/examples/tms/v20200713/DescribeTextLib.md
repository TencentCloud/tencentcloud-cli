**Example 1: 控制台获取用户词库列表**



Input: 

```
tccli tms DescribeTextLib --cli-unfold-argument  \
    --StrategyType 1
```

Output: 
```
{
    "Response": {
        "TextLib": [
            {
                "LibId": 1,
                "LibName": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

