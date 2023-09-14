**Example 1: 获取qps 弹性默认值**

获取qps 弹性默认值

Input: 

```
tccli waf GetInstanceQpsLimit --cli-unfold-argument  \
    --InstanceId abc
```

Output: 
```
{
    "Response": {
        "QpsData": {
            "ElasticBillingDefault": 1,
            "ElasticBillingMin": 1,
            "ElasticBillingMax": 1
        },
        "RequestId": "abc"
    }
}
```

