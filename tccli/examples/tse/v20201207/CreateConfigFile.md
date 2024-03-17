**Example 1: 新增配置文件**

新增配置文件

Input: 

```
tccli tse CreateConfigFile --cli-unfold-argument  \
    --InstanceId ins-fd191a86 \
    --ConfigFile.Name config-file-test-1 \
    --ConfigFile.Namespace Polaris \
    --ConfigFile.Group group-test-jayhjxu \
    --ConfigFile.Content test for CreateConfigFile
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "abc"
    }
}
```

