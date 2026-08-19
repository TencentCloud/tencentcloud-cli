**Example 1: 查询容器关联Web服务列表示例**



Input: 

```
tccli csip DescribeClusterContainerWebServiceList --cli-unfold-argument  \
    --ContainerId abc123def456
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "List": [
            {
                "Type": "nginx",
                "Version": "1.24.0",
                "RunAs": "nginx",
                "ExePath": "/usr/sbin/nginx",
                "ConfigPath": "/etc/nginx/conf.d/default.conf"
            }
        ],
        "RequestId": "5cd96106-1d72-466c-9bcf-9876543210ab"
    }
}
```

