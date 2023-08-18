**Example 1: 查询云服务详情示例**



Input: 

```
tccli iotvideo DescribeCloudStorageOrder --cli-unfold-argument  \
    --OrderId abc
```

Output: 
```
{
    "Response": {
        "StartTime": 1,
        "ExpireTime": 1,
        "PackageId": "abc",
        "Status": 1,
        "RequestId": "abc"
    }
}
```

