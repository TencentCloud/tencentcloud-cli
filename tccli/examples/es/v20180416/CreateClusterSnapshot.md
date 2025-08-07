**Example 1: 集群快照手动创建**



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
        "RequestId": "16eaxxxx-xxxx-xxxx-xxxx-xxxxxe45ae3c"
    }
}
```

