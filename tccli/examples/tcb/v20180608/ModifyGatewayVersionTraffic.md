**Example 1: 设置网关版本的流量比例接口实例**

设置安全网关不同版本流量比例

Input: 

```
tccli tcb ModifyGatewayVersionTraffic --cli-unfold-argument  \
    --EnvId env-test-xxx \
    --GatewayId gw-002 \
    --VersionsWeight.0.VersionName versionName-xxx \
    --VersionsWeight.0.Weight 50 \
    --VersionsWeight.1.VersionName versionName-yyy \
    --VersionsWeight.1.Weight 50
```

Output: 
```
{
    "Response": {
        "RequestId": "51a33e48-a808-4fe7-8c02-4e7be5245351"
    }
}
```

