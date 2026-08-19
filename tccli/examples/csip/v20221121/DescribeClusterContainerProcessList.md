**Example 1: 查询容器关联进程列表示例**



Input: 

```
tccli csip DescribeClusterContainerProcessList --cli-unfold-argument  \
    --ContainerId abc123def456 \
    --MemberId mem-*****************f66e429
```

Output: 
```
{
    "Response": {
        "TotalCount": 3,
        "List": [
            {
                "ProcessName": "nginx",
                "PID": 12345,
                "ContainerPID": 1,
                "ProcessPath": "/usr/sbin/nginx",
                "RunAs": "root",
                "StartTime": "2026-06-06T10:00:00+08:00"
            }
        ],
        "RequestId": "5cd96106-1d72-466c-9bcf-9876543210ab"
    }
}
```

