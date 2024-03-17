**Example 1: 创建连通性测试**



Input: 

```
tccli dts CreateConnectTestJob --cli-unfold-argument  \
    --JobId dts-xxxxx \
    --DatabaseType mysql \
    --Role src \
    --Endpoints.0.AccessType cdb \
    --Endpoints.0.Supplier others \
    --Endpoints.0.Region ap-chengdu \
    --Endpoints.0.Role src \
    --Endpoints.0.InstanceId cdb-ktexpqjo \
    --Endpoints.0.User root \
    --Endpoints.0.Password yuncloud#tes \
    --Endpoints.0.EncryptConn UnEncrypted
```

Output: 
```
{
    "Response": {
        "TaskIds": [
            25014
        ],
        "RequestId": "xxx"
    }
}
```

