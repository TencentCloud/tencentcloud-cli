**Example 1: 销毁集群节点**

销毁集群节点

Input: 

```
tccli emr TerminateClusterNodes --cli-unfold-argument  \
    --InstanceId emr-4zvc5mul \
    --CvmInstanceIds ins-42u6moui \
    --NodeFlag MASTER \
    --GraceDownTime 0 \
    --GraceDownFlag True
```

Output: 
```
{
    "Response": {
        "FlowId": 1000,
        "RequestId": "4d701c1e-8507-47e1-8c69-a8f06a236f24"
    }
}
```

