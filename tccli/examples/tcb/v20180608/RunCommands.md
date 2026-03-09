**Example 1: 查询一条数据**



Input: 

```
tccli tcb RunCommands --cli-unfold-argument  \
    --Tag tnt-nl7hjzasw \
    --MgoCommands.0.TableName luke_test \
    --MgoCommands.0.CommandType QUERY \
    --MgoCommands.0.Command {"find":"test","filter":{"_id":{"$eq":"1"}}}"}
```

Output: 
```
{
    "Response": {
        "Data": [
            "[\"{\\\"_id\\\":\\\"1\\\",\\\"category\\\":\\\"Web\\\",\\\"tags\\\":[\\\"JavaScript\\\",\\\"C#\\\"],\\\"date\\\":{\\\"$date\\\":{\\\"$numberLong\\\":\\\"1572937669786\\\"}}}\"]"
        ],
        "RequestId": "25785311-b03c-48d3-af34-36ff65e62d4a"
    }
}
```

