**Example 1: 设置文件系统配额**



Input: 

```
tccli cfs SetUserQuota --cli-unfold-argument  \
    --FileSystemId cfs-12345 \
    --UserType Uid \
    --UserId 1000 \
    --CapacityHardLimit 10 \
    --FileHardLimit 10000
```

Output: 
```
{
    "Response": {
        "RequestId": "fjo8aejo-fjei-32eu-2je9-fhue83nd81"
    }
}
```

