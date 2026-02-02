**Example 1: 校验集群是否可以添加只读分析引擎**

本接口（CheckCreateLibraDBInstance）用于校验集群是否可以添加只读分析引擎实例

Input: 

```
tccli cynosdb CheckCreateLibraDBInstance --cli-unfold-argument  \
    --ClusterId cynosdbmysql-6474meew \
    --InstanceId 
```

Output: 
```
{
    "Response": {
        "RequestId": "128046",
        "Status": "",
        "CheckItem": [
            {}
        ]
    }
}
```

