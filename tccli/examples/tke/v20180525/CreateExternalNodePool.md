**Example 1: 创建注册节点池**

创建注册节点池

Input: 

```
tccli tke CreateExternalNodePool --cli-unfold-argument  \
    --ClusterId cls-edk3h1cs \
    --Name 测试注册节点池 \
    --ContainerRuntime containerd \
    --RuntimeVersion 1.7.28
```

Output: 
```
{
    "Response": {
        "NodePoolId": "np-rpyicty0",
        "RequestId": "98b380d5-97d6-4ecc-9904-c0872168fc45"
    }
}
```

