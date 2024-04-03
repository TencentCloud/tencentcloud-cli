**Example 1: 修改HTTPS监听器绑定的证书**

修改HTTPS监听器绑定的证书

Input: 

```
tccli clb ModifyListener --cli-unfold-argument  \
    --ListenerId lbl-4fbxq45k \
    --Certificate.SSLMode UNIDIRECTIONAL \
    --Certificate.CertId Nb1DY3hQ \
    --LoadBalancerId lb-cuxw2rm0
```

Output: 
```
{
    "Response": {
        "RequestId": "b64574f9-5bc7-4a63-a9d7-3671b6a6d62b"
    }
}
```

**Example 2: 修改TCP监听器的名称、健康检查参数及转发策略**

修改TCP监听器的名称、健康检查参数及转发策略

Input: 

```
tccli clb ModifyListener --cli-unfold-argument  \
    --HealthCheck.UnHealthNum 5 \
    --HealthCheck.HealthNum 5 \
    --HealthCheck.IntervalTime 60 \
    --HealthCheck.TimeOut 35 \
    --HealthCheck.HealthSwitch 1 \
    --LoadBalancerId lb-cuxw2rm0 \
    --ListenerId lbl-d1ubsydq \
    --ListenerName newlis \
    --Scheduler LEAST_CONN \
    --SessionExpireTime 120
```

Output: 
```
{
    "Response": {
        "RequestId": "8cd88c83-fd30-47c0-8e7a-89bf13a7a83c"
    }
}
```

