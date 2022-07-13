**Example 1: 集群扩容**



Input: 

```
tccli emr ScaleOutInstance --cli-unfold-argument  \
    --InstanceId emr-5n3l5c83 \
    --TimeUnit s \
    --CoreCount 1 \
    --PayMode 0 \
    --TimeSpan 3600
```

Output: 
```
{
    "Response": {
        "BillId": "",
        "ClientToken": "",
        "DealNames": [
            "20200309357833",
            "20200309357834",
            "20200309357835",
            "20200309357836"
        ],
        "FlowId": 0,
        "InstanceId": "emr-5n3l5c83",
        "RequestId": "f0f11d21-6d0d-4f73-9177-8ae4ec456068"
    }
}
```

