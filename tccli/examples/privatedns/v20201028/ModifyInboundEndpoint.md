**Example 1: 修改入站终端节点**

修改入站终端节点

Input: 

```
tccli privatedns ModifyInboundEndpoint --cli-unfold-argument  \
    --EndpointId inbound-550ec54a46 \
    --EndpointName 终端节点1
```

Output: 
```
{
    "Response": {
        "RequestId": "ad9bfd8e-955d-471b-82d5-9b76d4b8fe23"
    }
}
```

