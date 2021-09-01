**Example 1: 修改终端节点服务属性**



Input: 

```
tccli vpc ModifyVpcEndPointServiceAttribute --cli-unfold-argument  \
    --AutoAcceptFlag True \
    --EndPointServiceName 测试 \
    --EndPointServiceId vpcsvc-kngiybxl \
    --VpcId vpc-hj3he929
```

Output: 
```
{
    "Response": {
        "RequestId": "fefb383a-7394-46c9-ba34-6b21e8fb3ac1"
    }
}
```

