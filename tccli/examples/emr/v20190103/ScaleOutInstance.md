**Example 1: 扩容节点**



Input: 

```
tccli emr ScaleOutInstance --cli-unfold-argument  \
    --TimeUnit s \
    --TimeSpan 3600 \
    --InstanceId  \
    --PayMode 0 \
    --ClientToken karpenter-15efec48d3bf2fa2 \
    --TaskCount 1 \
    --HardwareResourceType HOST \
    --ZoneId 100002 \
    --SubnetId subnet-lrcxwbju \
    --ResourceBaseType ComputeResource \
    --ComputeResourceId emr-cr-j91kjr07
```

Output: 
```
{
    "Response": {
        "BillId": "20260903326023549811631",
        "ClientToken": "karpenter-15efec48d3bf2fa2",
        "DealNames": [
            "20260903326023549811591"
        ],
        "FlowId": 0,
        "InstanceId": "emr-4hf4h9np",
        "TraceId": "1788433513-296027-78000019",
        "RequestId": "7208d49e-5c16-48fd-aa6e-2b10078bfb43"
    }
}
```

