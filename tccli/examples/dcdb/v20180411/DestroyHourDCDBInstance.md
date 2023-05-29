**Example 1: 销毁TDSQL按量计费实例**

销毁TDSQL按量计费实例

Input: 

```
tccli dcdb DestroyHourDCDBInstance --cli-unfold-argument  \
    --InstanceId tdsqlshard-avw0207d
```

Output: 
```
{
    "Response": {
        "RequestId": "8c4fba95-01e4-61d9-4146-59fc5afdf962",
        "FlowId": 100,
        "InstanceId": "tdsqlshard-avw0207d"
    }
}
```

