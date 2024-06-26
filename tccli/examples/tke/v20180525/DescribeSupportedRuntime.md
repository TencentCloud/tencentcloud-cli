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
                "RuntimeType": "docker",
                "RuntimeVersions": [
                    "1.12.4"
                ]
            }
        ],
        "RequestId": "207bd1e4-30de-4fac-b4fb-f9b15e2b4864"
    }
}
```

