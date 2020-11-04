**Example 1: 查询通道状态列表**



Input: 

```
tccli gaap DescribeProxiesStatus --cli-unfold-argument  \
    --ProxyIds link-1234abcd
```

Output: 
```
{
    "Response": {
        "InstanceStatusSet": [
            {
                "InstanceId": "link-4ftf12sb",
                "Status": "RUNNING"
            }
        ],
        "RequestId": "caac3323-bda3-4edc-b063-f584eb5936a2"
    }
}
```

