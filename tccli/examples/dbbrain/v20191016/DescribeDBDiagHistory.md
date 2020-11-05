**Example 1: Getting instance diagnosis event list**



Input: 

```
tccli dbbrain DescribeDBDiagHistory --cli-unfold-argument  \
    --StartTime '2019-01-01 00:00:00'\
    --EndTime '2019-01-01 01:00:00'\
    --InstanceId cdb-test
```

Output: 
```
{
    "Response": {
        "RequestId": "",
        "Events": [
            {
                "DiagType": "Row lock",
                "EndTime": "2019-07-08 15:17:20",
                "StartTime": "2019-07-08 15:51:08",
                "EventId": 5,
                "Severity": 4,
                "Outline": "Monitoring metric \"innodb_row_lock_waits\" triggered an alarm. Current value: 131",
                "DiagItem": "UPDATE statement row lock wait"
            }
        ]
    }
}
```

