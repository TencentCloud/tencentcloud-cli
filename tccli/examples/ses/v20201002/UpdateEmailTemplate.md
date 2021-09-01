**Example 1: 更新模板内容**



Input: 

```
tccli ses UpdateEmailTemplate --cli-unfold-argument  \
    --TemplateID 10091 \
    --TemplateName xx \
    --TemplateContent.Html PGh0bWw+dGhpcyBpcyBhIGV4YW1wbGUge3tjb2RlfX08L2h0bWw+ \
    --TemplateContent.Text dGhpcyBpcyBhIGV4YW1wbGU=
```

Output: 
```
{
    "Response": {
        "RequestId": "8979fc1e-9564-4fc9-bf7d-2958ce679b72"
    }
}
```

