**Example 1: 查询多个实例挂载的云硬盘数量**

查询多个实例挂载的云硬盘数量

Input: 

```
tccli cbs DescribeInstancesDiskNum --cli-unfold-argument  \
    --InstanceIds ins-9w5d2buw ins-jw0vit58
```

Output: 
```
{
    "Response": {
        "AttachDetail": [
            {
                "InstanceId": "ins-9w5d2buw",
                "AttachedDiskCount": 1,
                "MaxAttachCount": 10
            },
            {
                "InstanceId": "ins-jw0vit58",
                "AttachedDiskCount": 2,
                "MaxAttachCount": 10
            }
        ],
        "RequestId": "55db49cf-b9d7-da27-825b-5a02ba6884ca"
    }
}
```

