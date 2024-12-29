**Example 1: 请求示例**



Input: 

```
tccli live CreateLivePadTemplate --cli-unfold-argument  \
    --Url http://domain.com/app/name \
    --WaitDuration 1 \
    --Description pad \
    --MaxDuration 1 \
    --TemplateName name
```

Output: 
```
{
    "Response": {
        "TemplateId": 1000,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

