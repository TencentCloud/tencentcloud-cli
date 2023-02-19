**Example 1: 查询集群访问端口状态**

查询集群访问端口状态

Input: 

```
tccli tke DescribeClusterEndpointStatus --cli-unfold-argument  \
    --ClusterId cls-7ph3twqe
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Status": "Created",
        "ErrorMsg": "error"
    }
}
```

