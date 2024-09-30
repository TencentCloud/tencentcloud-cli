**Example 1: 查询边缘函数运行环境**



Input: 

```
tccli teo DescribeFunctionRuntimeEnvironment --cli-unfold-argument  \
    --ZoneId zone-kwsqufps \
    --FunctionId ef-xs2333
```

Output: 
```
{
    "Response": {
        "RequestId": "5f24d792-050d-439f-a864-353fd7b67e9f",
        "EnvironmentVariables": [
            {
                "Key": "name",
                "Type": "string",
                "Value": "edgeone"
            }
        ]
    }
}
```

