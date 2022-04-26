**Example 1: 查询维护时间窗口**



Input: 

```
tccli cdb DescribeTimeWindow --cli-unfold-argument  \
    --InstanceId cdb-eb2w7dto
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "MaxDelayTime": 10,
        "Monday": [
            "19:00-20:00"
        ],
        "Tuesday": [
            "18:00-20:00"
        ],
        "Friday": [
            "18:00-20:00"
        ],
        "Wednesday": [
            "18:00-20:00"
        ],
        "Thursday": [
            "18:00-20:00"
        ],
        "Sunday": [
            "18:00-20:00",
            "21:30-22:00"
        ],
        "Saturday": [
            "18:00-20:00"
        ]
    }
}
```

