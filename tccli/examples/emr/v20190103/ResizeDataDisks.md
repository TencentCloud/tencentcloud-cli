**Example 1: 云数据盘扩容**



Input: 

```
tccli emr ResizeDataDisks --cli-unfold-argument  \
    --InstanceId emr-xxxx \
    --CvmInstanceIds ins-xx \
    --DiskIds disk-xxx1 disk-xxx2 \
    --DiskSize 500
```

Output: 
```
{
    "Response": {
        "RequestId": "95eb9120-0883-407c-aa5a-43b4e2c250d1"
    }
}
```

