**Example 1: 删除卷快照**



Input: 

```
tccli camp DeleteVolumeSnapshot --cli-unfold-argument  \
    --ProjectID abc \
    --EnvironmentName abc \
    --ClusterID abc \
    --Name abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

**Example 2: 删除存储卷快照**



Input: 

```
tccli camp DeleteVolumeSnapshot --cli-unfold-argument  \
    --ProjectID prj-xxxxxxxx \
    --ClusterID cls-xxxxxxx \
    --EnvironmentName development \
    --Name xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "5976eb0f-ab70-4636-a2ba-522b3189e908"
    }
}
```

