**Example 1: 创建云应用服务**

创建云应用服务

Input: 

```
tccli tcb EstablishCloudBaseRunServer --cli-unfold-argument  \
    --Remark xx \
    --EnvId xx \
    --IsPublic True \
    --EsInfo.Index xx \
    --EsInfo.Account xx \
    --EsInfo.Ip xx \
    --EsInfo.Id 0 \
    --EsInfo.SecretName xx \
    --EsInfo.Password xx \
    --EsInfo.Port 0 \
    --ServiceName xx \
    --ImageRepo xx
```

Output: 
```
{
    "Response": {
        "Result": "xx",
        "RequestId": "xx"
    }
}
```

