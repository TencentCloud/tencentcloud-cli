**Example 1: 解隔离MariaDB按量计费实例**

解隔离MariaDB按量计费实例

Input: 

```
tccli mariadb ActivateHourDBInstance --cli-unfold-argument  \
    --InstanceIds tdsql-rlye31jd
```

Output: 
```
{
    "Response": {
        "FailedInstanceIds": [],
        "RequestId": "8ce27ff0-7fe1-11ea-8469-525400542aa6",
        "SuccessInstanceIds": [
            "tdsql-rlye31jd"
        ]
    }
}
```

