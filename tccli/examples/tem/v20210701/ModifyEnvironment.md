**Example 1: 编辑环境**

编辑环境

Input: 

```
tccli tem ModifyEnvironment --cli-unfold-argument  \
    --EnvironmentName name-xxx \
    --Description 这是一个描述 \
    --EnvironmentId en-xxxxxx \
    --SubnetIds subnet-xxxxxx \
    --SourceChannel 0 \
    --Vpc vpc-xxxxxx
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "xxx-xxx-xxx"
    }
}
```

