**Example 1: 开通指定可用区的边缘物理机计费能力**

为广州一区开通边缘物理机计费能力。

Input: 

```
tccli edgezone CreateEdgeNodeService --cli-unfold-argument  \
    --Zone ap-guangzhou-1
```

Output: 
```
{
    "Response": {
        "RequestId": "e5f6a789-4c3d-5b2e-af01-8d7c6b5a4e3f"
    }
}
```

