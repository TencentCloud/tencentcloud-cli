**Example 1: 查询参数模板协议端口关联的实例列表**

查询参数模板协议端口关联的实例列表

Input: 

```
tccli vpc DescribeServiceTemplateInstances --cli-unfold-argument  \
    --ServiceTemplateId ppm-12345678
```

Output: 
```
{
    "Response": {
        "RequestId": "5efe6fa7-6de2-4ce9-911a-f7438bf697d4"
    }
}
```

