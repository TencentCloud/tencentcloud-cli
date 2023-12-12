**Example 1: 关闭eks实例**

本示例用于关闭一个eks实例。

Input: 

```
tccli cxm StopInstances --cli-unfold-argument  \
    --InstanceIds eks-2v5gimnx \
    --StopType SOFT_FIRST
```

Output: 
```
{
    "Response": {
        "TaskId": 1171317945,
        "RequestId": "79bf28a4-2695-4d0e-92a9-8c5ec802b476"
    }
}
```

