**Example 1: 修改多写配置**

修改多写配置

Input: 

```
tccli monitor ModifyRemoteURLs --cli-unfold-argument  \
    --InstanceId prom-m4qf27hg \
    --RemoteWrites.0.URL http://172.30.0.9:9090/api/v1/prom/write \
    --RemoteWrites.0.BasicAuth.UserName user \
    --RemoteWrites.0.BasicAuth.Password pass
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

