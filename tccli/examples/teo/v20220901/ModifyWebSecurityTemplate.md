**Example 1: 修改策略模板名称**

修改 zone-2wkpkd52pku2 站点下 temp-cuwgt1ca 模板的名称为“Web防护标准模板V2”。

Input: 

```
tccli teo ModifyWebSecurityTemplate --cli-unfold-argument  \
    --ZoneId zone-2wkpkd52pku2 \
    --TemplateId temp-cuwgt1ca \
    --TemplateName Web防护标准模板V2
```

Output: 
```
{
    "Response": {
        "RequestId": "09ce3d28-1119-49cd-d5a9-27cb34dac669"
    }
}
```

