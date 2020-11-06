**Example 1: 集群扩容**



Input: 

```
tccli emr ScaleOutInstance --cli-unfold-argument  \
    --TimeUnit s \
    --TimeSpan 3600 \
    --CoreCount 1 \
    --InstanceId emr-5n3l5c83 \
    --PayMode 0
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

