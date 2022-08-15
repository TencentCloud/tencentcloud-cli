**Example 1: 修改云硬盘名称**

修改指定云硬盘名称为test_data_disk

Input: 

```
tccli cbs ModifyDiskAttributes --cli-unfold-argument  \
    --DiskName test_data_disk \
    --DiskIds disk-fyctkqsf
```

Output: 
```
{
    "Response": {
        "RequestId": "bf84fb00-6949-c0f6-aea8-5a1f806401c2"
    }
}
```

