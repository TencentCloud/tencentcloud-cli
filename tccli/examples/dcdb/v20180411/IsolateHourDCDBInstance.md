**Example 1: 隔离TDSQL按量计费实例**

隔离TDSQL按量计费实例

Input: 

```
tccli dcdb IsolateHourDCDBInstance --cli-unfold-argument  \
    --InstanceIds dcdbt-21dfpcv1
```

Output: 
```
{
    "Response": {
        "FailedInstanceIds": [],
        "RequestId": "204d03dc-2308-45e0-8ef8-aed2b3254e13",
        "SuccessInstanceIds": [
            "dcdbt-21dfpcv1"
        ]
    }
}
```

