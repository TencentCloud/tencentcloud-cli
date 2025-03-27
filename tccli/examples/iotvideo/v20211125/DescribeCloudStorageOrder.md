**Example 1: 查询云服务详情示例**



Input: 

```
tccli iotvideo DescribeCloudStorageOrder --cli-unfold-argument  \
    --OrderId id
```

Output: 
```
{
    "Response": {
        "StartTime": 1,
        "ExpireTime": 1,
        "PackageId": "yc",
        "Status": 1,
        "RequestId": "id",
        "ChannelId": 1
    }
}
```

