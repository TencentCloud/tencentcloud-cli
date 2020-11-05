**Example 1: Modifying the certificate bound to an HTTPS listener**



Input: 

```
tccli clb ModifyListener --cli-unfold-argument  \
    --LoadBalancerId lb-cuxw2rm0\
    --ListenerId lbl-4fbxq45k\
    --Certificate.SSLMode UNIDIRECTIONAL\
    --Certificate.CertId Nb1DY3hQ
```

Output: 
```
{
    "Response": {
        "RequestId": "b64574f9-5bc7-4a63-a9d7-3671b6a6d62b"
    }
}
```

**Example 2: Modifying the name, health check parameters, and forwarding policy of a TCP listener**



Input: 

```
tccli clb ModifyListener --cli-unfold-argument  \
    --LoadBalancerId lb-cuxw2rm0\
    --ListenerId lbl-d1ubsydq\
    --ListenerName newlis\
    --SessionExpireTime 120\
    --Scheduler LEAST_CONN\
    --HealthCheck.HealthSwitch 1\
    --HealthCheck.TimeOut 35\
    --HealthCheck.IntervalTime 60\
    --HealthCheck.HealthNum 5\
    --HealthCheck.UnHealthNum 5
```

Output: 
```
{
    "Response": {
        "RequestId": "8cd88c83-fd30-47c0-8e7a-89bf13a7a83c"
    }
}
```

