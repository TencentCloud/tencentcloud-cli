**Example 1: 创建环境**

创建环境

Input: 

```
tccli tem CreateEnvironment --cli-unfold-argument  \
    --EnvironmentName name-xxx \
    --Description 这是一个描述 \
    --K8sVersion 1.69.1 \
    --SubnetIds subnet-xxx \
    --EnableTswTraceService True \
    --SourceChannel 0 \
    --Vpc vpc-1n5javez
```

Output: 
```
{
    "Response": {
        "RequestId": "81f74023-563c-437d-abf7-8139449ef178",
        "Result": "en-xxxx"
    }
}
```

