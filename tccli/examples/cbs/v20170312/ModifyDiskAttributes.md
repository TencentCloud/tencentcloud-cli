**Example 1: 修改云硬盘名称**



Input: 

```
tccli cbs ModifyDiskAttributes --cli-unfold-argument  \
    --DiskIds disk-fyctkqsf\
    --DiskName test_data_disk
```

Output: 
```
{
    "Response": {
        "RequestId": "bf84fb00-6949-c0f6-aea8-5a1f806401c2"
    }
}
```

**Example 2: 修改云盘类型**

将一块弹性数据盘，付费模式为预付费，从普通云盘升级为高性能云盘，云盘大小 100G，当前未挂载。

Input: 

```
tccli cbs ModifyDiskAttributes --cli-unfold-argument  \
    --DiskIds disk-hdz4c824\
    --DiskType CLOUD_PREMIUM
```

Output: 
```
{
    "Response": {
        "RequestId": "d010c751-3edb-4388-878c-1de0891aa1fd"
    }
}
```

