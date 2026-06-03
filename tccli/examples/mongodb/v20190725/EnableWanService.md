**Example 1: 开启实例的外网访问地址。**

实例未开启外网访问，请求该接口开启外网访问。

Input: 

```
tccli mongodb EnableWanService --cli-unfold-argument  \
    --InstanceId cmgo-qwla**** \
    --LoadBalancerId lb-94d6**** \
    --NodeList.0.VipVport 10.0.30.*:27017 \
    --NodeList.0.ListenerPort 10001 \
    --NodeList.1.VipVport 10.0.30.*:27017 \
    --NodeList.1.ListenerPort 10002 \
    --NodeList.2.VipVport 10.0.30.1*:27017 \
    --NodeList.2.ListenerPort 10003
```

Output: 
```
{
    "Response": {
        "FlowId": 174548484400,
        "RequestId": "ce73f291-7ffd-4390-9434-7c****12sa1b0"
    }
}
```

