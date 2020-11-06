**Example 1: Modifying instance parameters**



Input: 

```
tccli redis ModifyInstanceParams --cli-unfold-argument  \
    --InstanceId crs-5a4py64p \
    --InstanceParams.0.Key timeout \
    --InstanceParams.0.Value 120
```

Output: 
```
{
    "Response": {
        "Changed": false,
        "TaskId": 327,
        "RequestId": "e546784b-709c-401d-aba6-73037eb4e522"
    }
}
```

