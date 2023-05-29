**Example 1: 隔离MariaDB按量计费实例**

隔离MariaDB按量计费实例

Input: 

```
tccli mariadb IsolateHourDBInstance --cli-unfold-argument  \
    --InstanceIds tdsql-cq3ndzu7
```

Output: 
```
{
    "Response": {
        "FailedInstanceIds": [],
        "RequestId": "8ce27ff0-7fe1-11ea-8469-525400542aa6",
        "SuccessInstanceIds": []
    }
}
```

