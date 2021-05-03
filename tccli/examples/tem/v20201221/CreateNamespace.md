**Example 1: 创建环境（命名空间）**

创建环境（命名空间）

Input: 

```
tccli tem CreateNamespace --cli-unfold-argument  \
    --NamespaceName xx \
    --K8sVersion 1.16.9 \
    --SubnetIds xx \
    --Description xx \
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

