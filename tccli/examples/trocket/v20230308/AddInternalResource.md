**Example 1: 添加4.x物理集群资源**



Input: 

```
tccli trocket AddInternalResource --cli-unfold-argument  \
    --ClusterName rmqbroker-bad \
    --AdminUrl 1.1.1.1:9876 \
    --AdminToken a123dfbaddf \
    --PublicEndpoint a.com \
    --VpcEndpoint b.com \
    --HttpPublicEndpoint a.com \
    --HttpVpcEndpoint b.com
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "RequestId": "10a425cc-c099-411e-a642-3862388a9d8e"
    }
}
```

