**Example 1: 删除安全策略配置模板**

删除 zone-2wkpkd52pku8 站点下的 temp-o3xctdd2 安全策略模板。

Input: 

```
tccli teo DeleteWebSecurityTemplate --cli-unfold-argument  \
    --ZoneId zone-2wkpkd52pku8 \
    --TemplateId temp-o3xctdd2
```

Output: 
```
{
    "Response": {
        "RequestId": "09ce3d28-1119-49cd-f0e3-27cb34dac669"
    }
}
```

