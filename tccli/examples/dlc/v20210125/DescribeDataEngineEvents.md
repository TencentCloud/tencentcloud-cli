**Example 1: test**



Input: 

```
tccli dlc DescribeDataEngineEvents --cli-unfold-argument  \
    --Limit 0 \
    --DataEngineName xx \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Events": [
            {
                "Time": "2021-12-15 19:43:08",
                "EventsAction": "集群扩容",
                "ClusterInfo": "扩容前：集群个数0个，集群规模16CU，扩容后:集群个数1个，集群规模16CU"
            }
        ],
        "Page": 1,
        "TotalCount": 1,
        "RequestId": "4eeb6764-d552-4d9b-89ac-62034195e936",
        "Size": 10,
        "TotalPages": 1
    }
}
```

