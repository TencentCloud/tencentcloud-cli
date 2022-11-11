**Example 1: 删除文件系统配额**



Input: 

```
tccli cfs DeleteUserQuota --cli-unfold-argument  \
    --FileSystemId cfs-12345 \
    --UserType Uid \
    --UserId 1000
```

Output: 
```
{
    "Response": {
        "RequestId": "fjo8aejo-fjei-32eu-2je9-fhue83nd81"
    }
}
```

