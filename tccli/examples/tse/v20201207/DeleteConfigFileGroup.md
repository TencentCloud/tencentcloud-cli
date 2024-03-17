**Example 1: 删除配置文件分组**

删除配置文件分组

Input: 

```
tccli tse DeleteConfigFileGroup --cli-unfold-argument  \
    --InstanceId janice-test \
    --Namespace namespace_1 \
    --Group group_1
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "63d46143-c731-4aff-b0c9-edce7401db32"
    }
}
```

