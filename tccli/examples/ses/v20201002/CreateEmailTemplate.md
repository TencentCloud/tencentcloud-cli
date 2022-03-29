**Example 1: 创建HTML邮件模板**



Input: 

```
tccli ses CreateEmailTemplate --cli-unfold-argument  \
    --TemplateContent.Html PGh0bWw+dGhpcyBpcyBhIGV4YW1wbGUge3tjb2RlfX08L2h0bWw+ \
    --TemplateName TestName
```

Output: 
```
{
    "Response": {
        "RequestId": "8979fc1e-9564-4fc9-bf7d-2958ce679b72",
        "TemplateID": 123
    }
}
```

**Example 2: 创建文本邮件模板**



Input: 

```
tccli ses CreateEmailTemplate --cli-unfold-argument  \
    --TemplateContent.Text dGhpcyBpcyBhIGV4YW1wbGUge3tjb2RlfX0= \
    --TemplateName TestName
```

Output: 
```
{
    "Response": {
        "RequestId": "8979fc1e-9564-4fc9-bf7d-2958ce679b72",
        "TemplateID": 123
    }
}
```

