**Example 1: demo**



Input: 

```
tccli es CreateClusterSnapshot --cli-unfold-argument  \
    --InstanceId es-xxx \
    --SnapshotName es-xxx-test_20240912 \
    --Indices kibana_sample_data_flights
```

Output: 
```
{
    "Response": {
        "InstanceId": "es-xxx",
        "RequestId": "abc"
    }
}
```

