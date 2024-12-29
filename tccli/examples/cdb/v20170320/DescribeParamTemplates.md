**Example 1: 查询参数模板列表**



Input: 

```
tccli cdb DescribeParamTemplates --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Items": [
            {
                "TemplateId": 2333,
                "Name": "andy",
                "Description": "5.7",
                "EngineVersion": "5.7",
                "TemplateType": "HIGH_STABILITY",
                "EngineType": "InnoDB"
            }
        ],
        "RequestId": "756bb037-a44a-4b4f-abe0-6efd34a6c792"
    }
}
```

