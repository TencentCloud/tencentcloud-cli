**Example 1: 修改健康检查模板的名称**



Input: 

```
tccli alb ModifyHealthCheckTemplate --cli-unfold-argument  \
    --HealthCheckTemplateId hct-fb7tuf7o \
    --HealthCheckTemplateName 修改名称
```

Output: 
```
{
    "Response": {
        "RequestId": "e109ac6e-a12b-4fb2-885e-e63d63c4d883"
    }
}
```

