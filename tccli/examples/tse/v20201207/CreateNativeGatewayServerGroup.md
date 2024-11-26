**Example 1: 创建云原生网关引擎分组**

创建云原生网关引擎分组

Input: 

```
tccli tse CreateNativeGatewayServerGroup --cli-unfold-argument  \
    --GatewayId gateway-dde03767 \
    --Name 公网入口分组 \
    --NodeConfig.Specification 1c2g \
    --NodeConfig.Number 3 \
    --SubnetId subnet-8tzp8ugx \
    --Description 公网入口分组 \
    --InternetMaxBandwidthOut 5 \
    --InternetConfig.InternetAddressVersion IPV4 \
    --InternetConfig.InternetPayMode TRAFFIC \
    --InternetConfig.InternetMaxBandwidthOut 5 \
    --InternetConfig.Description 公网入口分组 \
    --InternetConfig.SlaType clb.c4.small
```

Output: 
```
{
    "Response": {
        "Result": {
            "GatewayId": "gateway-dde03767",
            "GroupId": "group-dde0376z",
            "Status": "Creating",
            "TaskId": "task-adfq1a3z"
        },
        "RequestId": "af9a7054-e0f0-4421-95ce-d4f95b7cdf96"
    }
}
```

