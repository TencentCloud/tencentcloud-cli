**Example 1: 示例**



Input: 

```
tccli gs DistributeAndroidInstanceImageToHosts --cli-unfold-argument  \
    --HostSerialNumbers RK8S50P1402309016 RK8S50P1402309017 \
    --ImageId image-49va6apu
```

Output: 
```
{
    "Response": {
        "RequestId": "cb50f61b-6058-4500-b742-a692e06d3ef3",
        "TaskSet": [
            {
                "HostSerialNumber": "RK8S50P1402309016",
                "TaskId": "4e4af02c-7977-4612-8974-5b6a8493fa0c"
            },
            {
                "HostSerialNumber": "RK8S50P1402309017",
                "TaskId": "873b2107-4422-426f-9356-0a7ecb605297"
            }
        ]
    }
}
```

