**Example 1: 删除配置文件**

删除配置文件

Input: 

```
tccli tse DeleteConfigFiles --cli-unfold-argument  \
    --InstanceId ins-fd191a86 \
    --Namespace Polaris \
    --Group group-test-jayhjxu \
    --Name config-file-test
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

