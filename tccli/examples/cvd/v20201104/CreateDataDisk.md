**Example 1: 实例新增数据盘**



Input: 

```
tccli cvd CreateDataDisk --cli-unfold-argument  \
    --InstanceId cdi-ubnpcatzru20umw \
    --DiskType CLOUD_SSD \
    --DiskSize 50
```

Output: 
```
{
    "Response": {
        "RequestId": "c2c80067-8289-434c-ad4c-789269a4f7a8"
    }
}
```

