**Example 1: 编辑环境**

编辑环境

Input: 

```
tccli tem ModifyEnvironment --cli-unfold-argument  \
    --EnvironmentName xx \
    --Description xx \
    --EnvironmentId xx \
    --SubnetIds xx \
    --SourceChannel 0 \
    --Vpc xx
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "xx"
    }
}
```

