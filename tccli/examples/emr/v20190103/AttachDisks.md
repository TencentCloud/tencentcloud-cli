**Example 1: 云盘挂载**



Input: 

```
tccli emr AttachDisks --cli-unfold-argument  \
    --InstanceId emr-xxxx \
    --DiskIds disk-xxx1 disk-xxx2
```

Output: 
```
{
    "Response": {
        "RequestId": "95eb9120-0883-407c-aa5a-43b4e2c250d1"
    }
}
```

