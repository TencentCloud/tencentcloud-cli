**Example 1: 查询运行参数模板列表**



Input: 

```
tccli omics DescribeInputTemplates --cli-unfold-argument  \
    --ProjectId prj-efficient-maroon-slug-075080 \
    --Limit 10 \
    --Offset 0 \
    --ApplicationVersionId 0 \
    --ApplicationId app-remarkable-bleak-terrier-617099
```

Output: 
```
{
    "Response": {
        "InputTemplates": [
            {
                "ApplicationId": "in-best-teal-gorilla-731558",
                "ApplicationVersionId": "0",
                "Creator": "chanh_test",
                "CreatorId": "a7a67c817c5b4012adde352c045295ba",
                "Description": "",
                "InputTemplateId": "in-best-teal-gorilla-731558",
                "Name": "test-template",
                "ProjectId": "prj-efficient-maroon-slug-075080",
                "Uuid": "0e5c1233-bdad-4541-9e15-39f39a46c934"
            }
        ],
        "TotalCount": 1,
        "RequestId": "8e319121-625f-40d3-876c-103b74159ef8"
    }
}
```

