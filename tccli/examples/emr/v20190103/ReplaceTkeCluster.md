**Example 1: EMR on TKE更换依赖的容器集群**

EMR on TKE更换依赖的容器集群

Input: 

```
tccli emr ReplaceTkeCluster --cli-unfold-argument  \
    --InstanceId emr-99xihnsh \
    --TkeClusterId cls-p3yh0ik2 \
    --Platform tke
```

Output: 
```
{
    "Response": {
        "FlowId": 88,
        "RequestId": "3efac2e7-d9d9-4f85-b8e4-11a700f6dfb3"
    }
}
```

