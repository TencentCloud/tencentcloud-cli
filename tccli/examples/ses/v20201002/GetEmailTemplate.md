**Example 1: 获取模板内容**



Input: 

```
tccli ses GetEmailTemplate --cli-unfold-argument  \
    --TemplateID 10091
```

Output: 
```
{
    "Response": {
        "TemplateStatus": 1,
        "RequestId": "8979fc1e-9564-4fc9-bf7d-2958ce679b72",
        "TemplateContent": {
            "Html": "PGh0bWw+dGhpcyBpcyBhIGV4YW1wbGUge3tjb2RlfX08L2h0bWw+",
            "Text": "dGhpcyBpcyBhIGV4YW1wbGU="
        },
        "TemplateName": "模板名称"
    }
}
```

