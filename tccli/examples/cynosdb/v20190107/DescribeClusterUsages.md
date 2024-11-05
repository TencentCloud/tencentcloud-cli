**Example 1: 集群用量拉取**



Input: 

```
tccli cynosdb DescribeClusterUsages --cli-unfold-argument  \
    --EndTime 2021-05-27 23:59:59 \
    --ClusterId cynosdbmysql-xxx \
    --Period 86400 \
    --StartTime 2021-05-27 00:00:00
```

Output: 
```
{
    "Response": {
        "Usages": [
            {
                "Ccu": 0,
                "Timestamp": 1621987200,
                "Storage": 0
            },
            {
                "Ccu": 0,
                "Timestamp": 1622073600,
                "Storage": 0
            }
        ],
        "RequestId": "3b92a362-bf84-11eb-bf89-525400b7dd5a"
    }
}
```

