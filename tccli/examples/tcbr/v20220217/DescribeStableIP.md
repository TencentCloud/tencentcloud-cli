**Example 1: 查询固定IP地址**



Input: 

```
tccli tcbr DescribeStableIP --cli-unfold-argument  \
    --EnvId test-1gbtbgkjf8f48e2c
```

Output: 
```
{
    "Response": {
        "Address": "1.1.1.1",
        "Status": "normal",
        "ExpireTime": "2022-12-06 00:00:00",
        "RequestId": "requestid"
    }
}
```

