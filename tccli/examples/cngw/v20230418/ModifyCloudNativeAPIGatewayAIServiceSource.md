**Example 1: 更新AI服务来源**



Input: 

```
tccli cngw ModifyCloudNativeAPIGatewayAIServiceSource --cli-unfold-argument  \
    --GatewayId gateway-9a766f25 \
    --SourceName nacos-registry2 \
    --SourceType Registry \
    --SourceId ins-f334b584 \
    --Description 普通注册中心 \
    --SourceInfo.InstanceId ins-f334b584 \
    --SourceInfo.Auth.Username ***** \
    --SourceInfo.Auth.Password ********
```

Output: 
```
{
    "Response": {
        "RequestId": "47a9fed1-76ae-46f8-bc10-dde0763e718d"
    }
}
```

