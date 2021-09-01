**Example 1: 查询集群开启端口流程状态**



Input: 

```
tccli tke DescribeClusterEndpointVipStatus --cli-unfold-argument  \
    --ClusterId cls-xxxxxxxx,
```

Output: 
```
{
    "Response": {
        "Status": "Creating",
        "ErrorMsg": "",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

