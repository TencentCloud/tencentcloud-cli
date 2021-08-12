**Example 1: 创建环境**

创建环境

Input: 

```
tccli tem CreateEnvironment --cli-unfold-argument  \
    --EnvironmentName xx \
    --Description xx \
    --K8sVersion xx \
    --SubnetIds xx \
    --EnableTswTraceService True \
    --SourceChannel 0 \
    --Vpc xx
```

Output: 
```
{
    "Response": {
        "RequestId": "81f74023-563c-437d-abf7-8139449ef178",
        "Result": "env-xxxx"
    }
}
```

