**Example 1: 创建云原生网关引擎分组**

创建云原生网关引擎分组

Input: 

```
tccli tse CreateNativeGatewayServerGroup --cli-unfold-argument  \
    --GatewayId abc \
    --Name abc \
    --NodeConfig.Specification abc \
    --NodeConfig.Number 0 \
    --SubnetId abc \
    --Description abc \
    --InternetMaxBandwidthOut 1 \
    --InternetConfig.InternetAddressVersion abc \
    --InternetConfig.InternetPayMode abc \
    --InternetConfig.InternetMaxBandwidthOut 1 \
    --InternetConfig.Description abc \
    --InternetConfig.SlaType abc
```

Output: 
```
{
    "Response": {
        "Result": {
            "GatewayId": "abc",
            "GroupId": "abc",
            "Status": "abc",
            "TaskId": "abc"
        },
        "RequestId": "abc"
    }
}
```

