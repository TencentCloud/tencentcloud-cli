**Example 1: 查询攻击溯源**

查询攻击溯源

Input: 

```
tccli cwp DescribeAttackSourceEvents --cli-unfold-argument  \
    --BeginDate 2020-09-22 \
    --EndDate 2020-09-22 \
    --Uuid xx \
    --EventInfoParam dsss
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "Uuid": "xx",
                "Level": 1,
                "EventType": 1,
                "Content": "xx",
                "CreatedTime": "xx",
                "LevelZh": "xx",
                "Id": 1
            }
        ],
        "RequestId": "xx"
    }
}
```

