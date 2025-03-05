**Example 1: 设置文件系统用户配额**



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

**Example 2: 设置文件系统目录配额**

POST / HTTP/1.1
Host: cfs.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: SetUserQuota
<公共请求参数>

{
    "FileSystemId": "cfs-12345",
    "UserType": "Dir",
    "DirectoryPath": "/cfs/123",
    "CapacityHardLimit":  10,
    "FileHardLimit":  10000
}

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
        "RequestId": "fasfsaaejo-fjei-32eu-2je9-fhue83nd81"
    }
}
```

