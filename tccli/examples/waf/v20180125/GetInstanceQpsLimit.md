**Example 1: 获取qps 弹性默认值**

获取qps 弹性默认值

Input: 

```
tccli waf GetInstanceQpsLimit --cli-unfold-argument  \
    --InstanceId waf_22piczpx8beg7rht
```

Output: 
```
{
    "Response": {
        "QpsData": {
            "ElasticBillingDefault": 1,
            "ElasticBillingMin": 1,
            "ElasticBillingMax": 1,
            "QPSExtendMax": 1,
            "QPSExtendIntlMax": 1
        },
        "RequestId": "d55b94a8-07bb-4326-b82f-e6678151afe0"
    }
}
```

