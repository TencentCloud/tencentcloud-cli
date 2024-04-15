**Example 1: 获取运行时版本信息**



Input: 

```
tccli tke DescribeSupportedRuntime --cli-unfold-argument  \
    --K8sVersion xxxx
```

Output: 
```
{
    "Response": {
        "OptionalRuntimes": [
            {
                "RuntimeType": "docker"
            }
        ],
        "RequestId": "xx"
    }
}
```

