**Example 1: 黑石托管机器移除子网**



Input: 

```
tccli bmvpc DeleteHostedInterface --cli-unfold-argument  \
    --VpcId vpc-34cxlz7z \
    --SubnetId subnet-1oo8hlkg \
    --InstanceIds chm-343fqw4
```

Output: 
```
{
    "Response": {
        "ResourceIds": [
            "chm-343fqw4"
        ],
        "TaskId": 20871,
        "RequestId": "bd15d748-8c81-450b-8a40-91e883ff38d6"
    }
}
```

