**Example 1: 创建环境（命名空间）**

创建环境（命名空间）

Input: 

```
tccli tem CreateResource --cli-unfold-argument  \
    --NamespaceId env-xx \
    --ResourceType VPC \
    --ResourceId vpc-xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "81f74023-563c-437d-abf7-8139449ef178",
        "Result": true
    }
}
```

