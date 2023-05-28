**Example 1: 解隔离TDSQL按量计费实例**

解隔离TDSQL按量计费实例

Input: 

```
tccli dcdb ActiveHourDCDBInstance --cli-unfold-argument  \
    --InstanceIds tdsqlshard-cq3ndzu7
```

Output: 
```
{
    "Response": {
        "FailedInstanceIds": [],
        "RequestId": "8ce27ff0-7fe1-11ea-8469-525400542aa6",
        "SuccessInstanceIds": [
            "tdsqlshard-cq3ndzu7"
        ]
    }
}
```

