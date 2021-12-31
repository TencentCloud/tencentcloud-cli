**Example 1: 查询实例挂载云盘数量**



Input: 

```
tccli lighthouse DescribeInstancesDiskNum --cli-unfold-argument  \
    --InstanceIds lhins-anxwfvxh
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AttachDetailSet": [
            {
                "InstanceId": "lhins-anxwfvxh",
                "AttachedDiskCount": 1,
                "MaxAttachCount": 5
            }
        ],
        "RequestId": "3a73da61-4f9a-453b-bc11-553383f5d59d"
    }
}
```

