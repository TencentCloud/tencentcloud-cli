**Example 1: 测试请求cube内部接口**

测试请求cube内部接口

Input: 

```
tccli cube RunProxyCall --cli-unfold-argument  \
    --ProxyProduct cube \
    --ProxyAction DescribeInstances \
    --ProxyRequest {} \
    --ProxyRegion ap-chongqing \
    --UserAppId 123456
```

Output: 
```
{
    "Response": {
        "ProxyResult": "{\"Response\":{\"InstanceSet\":[],\"RequestId\":\"60086dbb-5382-4db7-a831-f96aa5dc0e5b\",\"TotalCount\":2}}",
        "RequestId": "79e51a32-a963-45e0-ab84-dadb0de737de"
    }
}
```

