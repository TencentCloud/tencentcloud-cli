**Example 1: Modifying the Name of a Cloud Disk**



Input: 

```
tccli cbs ModifyDiskAttributes --cli-unfold-argument  \
    --DiskIds disk-fyctkqsf \
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

**Example 2: Modifying the Type of the Cloud Disk**

Upgrade an HDD elastic cloud disk to a premium cloud disk, which is 100 GB in size and is not currently mounted.

Input: 

```
tccli cbs ModifyDiskAttributes --cli-unfold-argument  \
    --DiskIds disk-hdz4c824 \
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

