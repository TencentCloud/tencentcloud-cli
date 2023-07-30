**Example 1: 查询镜像kernel示例**

查询镜像kernel示例

Input: 

```
tccli tione DescribeNotebookImageKernels --cli-unfold-argument  \
    --NotebookId nb-6763738683264283
```

Output: 
```
{
    "Response": {
        "Kernels": [
            "pytorch_py3"
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

