**Example 1: 实例系统盘扩容示例**

实例系统盘扩容

Input: 

```
tccli cvd ModifyDiskConfiguration --cli-unfold-argument  \
    --InstanceId cdi-krxgg2id76erx4f \
    --NewSystemDisk.DiskType CLOUD_SSD \
    --NewSystemDisk.DiskSize 70 \
    --NewSystemDisk.DiskId disk-oalp79e1
```

Output: 
```
{
    "Response": {
        "RequestId": "1bd1ccd0-74c6-48c3-a525-3dfc3637d9ee"
    }
}
```

