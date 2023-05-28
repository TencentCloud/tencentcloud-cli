**Example 1: 隔离TDSQL包年包月实例**

隔离TDSQL包年包月实例

Input: 

```
tccli dcdb IsolateDCDBInstance --cli-unfold-argument  \
    --InstanceIds tdsqlshard-pevrkilh
```

Output: 
```
{
    "Response": {
        "FailedInstanceIds": [],
        "RequestId": "e3b9a860-5864-43b2-8f0f-9684dea8fa58",
        "SuccessInstanceIds": [
            "tdsqlshard-pevrkilh"
        ]
    }
}
```

