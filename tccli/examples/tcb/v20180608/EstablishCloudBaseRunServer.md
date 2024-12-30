**Example 1: 创建云应用服务**

创建云应用服务

Input: 

```
tccli tcb EstablishCloudBaseRunServer --cli-unfold-argument  \
    --Remark  \
    --EnvId  \
    --IsPublic True \
    --EsInfo.Index  \
    --EsInfo.Account  \
    --EsInfo.Ip  \
    --EsInfo.Id 0 \
    --EsInfo.SecretName  \
    --EsInfo.Password  \
    --EsInfo.Port 0 \
    --ServiceName  \
    --ImageRepo 
```

Output: 
```
{
    "Response": {
        "Result": "succ",
        "RequestId": "sdfsdff"
    }
}
```

