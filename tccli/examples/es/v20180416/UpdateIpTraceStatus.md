**Example 1: 更新ES集群IP溯源状态**



Input: 

```
tccli es UpdateIpTraceStatus --cli-unfold-argument  \
    --InstanceId es-xasdadas \
    --FilterKibanaIp False \
    --OpenIpTrace False \
    --DurationTime 0 \
    --IpTraceConfig.EnableRequest False \
    --IpTraceConfig.EnableResponse False \
    --IpTraceConfig.EnableRequestBody False \
    --IpTraceConfig.EnableResponseBody False \
    --IpTraceConfig.RemoteIpInclude  \
    --IpTraceConfig.RemoteIpExclude  \
    --IpTraceConfig.UriInclude  \
    --IpTraceConfig.UriExclude 
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

