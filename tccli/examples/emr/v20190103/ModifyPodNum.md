**Example 1: 调整容器集群Pod数量**

调整容器集群Pod数量

Input: 

```
tccli emr ModifyPodNum --cli-unfold-argument  \
    --InstanceId emr-ikoyp9nw \
    --ServiceGroup 44 \
    --ServiceType 93 \
    --PodNum 3
```

Output: 
```
{
    "Response": {
        "InstanceId": "emr-ikoyp9nw",
        "FlowId": 0,
        "RequestId": "fe127236-3646-4676-80ae-a491b596fedd"
    }
}
```

