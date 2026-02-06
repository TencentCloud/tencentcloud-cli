**Example 1: 创建用户vpc连接到引擎网络**

创建用户vpc连接到引擎网络

Input: 

```
tccli dlc CreateUserVpcConnection --cli-unfold-argument  \
    --UserVpcId vpc-dk19yfxx \
    --UserSubnetId subnet-gne3mgxx \
    --UserVpcEndpointName rickytest \
    --EngineNetworkId DataEngine-Network-xxx \
    --UserVpcEndpointVip 10.0.0.13
```

Output: 
```
{
    "Response": {
        "UserVpcEndpointId": "vpce-h4czuhxx",
        "RequestId": "515ee497-d527-4f05-b484-61b46522a408"
    }
}
```

