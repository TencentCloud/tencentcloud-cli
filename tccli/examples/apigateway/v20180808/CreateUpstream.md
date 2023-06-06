**Example 1: 创建vpc通道**

用于创建vpc通道

Input: 

```
tccli apigateway CreateUpstream --cli-unfold-argument  \
    --Retries 1 \
    --UpstreamName test \
    --Algorithm ROUND_ROBIN \
    --UniqVpcId vpc-sadada \
    --UpstreamType IP_PORT \
    --UpstreamHost www.a.com \
    --UpstreamDescription test \
    --Scheme instance-HTTP \
    --Nodes.0.VmInstanceId ins-saadas \
    --Nodes.0.Host 127.0.0.1 \
    --Nodes.0.Port 80 \
    --Nodes.0.Weight 100
```

Output: 
```
{
    "Response": {
        "UpstreamId": "upstream-0c96l2bo",
        "RequestId": "b3197c48-53fb-46df-b721-df4424cf8be9"
    }
}
```

