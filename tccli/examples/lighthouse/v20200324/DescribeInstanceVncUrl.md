**Example 1: 查询实例管理终端地址**

本示例用于查询实例管理终端地址。

Input: 

```
tccli lighthouse DescribeInstanceVncUrl --cli-unfold-argument  \
    --InstanceId lhins-ruy9d2tw
```

Output: 
```
{
    "Response": {
        "InstanceVncUrl": "wss%3A%2F%2Fusevnc.qcloud.com%3A443%2Fvnc%3Fs%3DTnVQUEpVYkc4eUMvMEkyUERKUjhRbzJhbGcyWHFaWmVMU1dRbUQwd0hVVHo2WU4wOEpLWjlQd0JVSWQwUXZOK2FDcWlOdDJIbUJxSTZDL0RXcHZxYnZZMmRkWWZWcEZia2lyb09XMzdKNmM9%26password%3D%26isWindows%3Dfalse%26isUbuntu%3Dfalse",
        "RequestId": "f9f6fa33-679c-40ea-bb30-b1e9a8989305"
    }
}
```

