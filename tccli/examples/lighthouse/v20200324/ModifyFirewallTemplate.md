**Example 1: 修改防火墙模板**

修改防火墙模板名称

Input: 

```
tccli lighthouse ModifyFirewallTemplate --cli-unfold-argument  \
    --TemplateId lhft-6brh0ciy \
    --TemplateName test-modify
```

Output: 
```
{
    "Response": {
        "RequestId": "cc75e4c9-b6a9-44c2-9a8f-ef8e78ff0e81"
    }
}
```

