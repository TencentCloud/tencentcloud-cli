**Example 1: 请求示例**



Input: 

```
tccli redis DescribeParamTemplates --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "0e728fa9-c2e5-4bf8-8d6b-c1c4fab7b6db",
        "Items": [
            {
                "Name": "CustomParamTemplate",
                "Description": "MyCustomParamTemplate",
                "ProductType": 6,
                "TemplateId": "crs-cfg-sa23d5d3"
            }
        ]
    }
}
```

