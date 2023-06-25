**Example 1: 创建托管集群外网访问端口**

创建托管集群外网访问端口

Input: 

```
tccli tke CreateClusterEndpointVip --cli-unfold-argument  \
    --ClusterId cls-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestFlowId": "100000",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

