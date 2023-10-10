**Example 1: 查询攻击溯源**

查询攻击溯源

Input: 

```
tccli cwp DescribeAttackSource --cli-unfold-argument  \
    --BeginDate 2020-09-22 \
    --EndDate 2020-09-22 \
    --Uuid xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "AttackSource": {
            "EventInfoParam": "xx",
            "Nodes": [
                {
                    "EventId": 1,
                    "Level": 1,
                    "EventType": "xx",
                    "NodeDesc": "xx",
                    "NodeId": "xx",
                    "StartTime": "xx",
                    "Ip": "xx",
                    "EndTime": "xx"
                }
            ],
            "Edges": [
                {
                    "To": "xx",
                    "From": "xx"
                }
            ]
        }
    }
}
```

