**Example 1: 查询合同对比任务结果**

本接口（DescribeContractComparisonTask）用于查询合同对比任务结果详情。

Input: 

```
tccli ess DescribeContractComparisonTask --cli-unfold-argument  \
    --Operator.UserId yDwqbUUckp3o2rzmUxHsV0j1FlhYIKo7 \
    --TaskId yDtrrUUckp94goxhUyjVZ8rSEQ0lg7vb
```

Output: 
```
{
    "Response": {
        "AddDiffCount": 7,
        "ChangeDiffCount": 2,
        "Comment": "备注备注备注",
        "CreateTime": 1758526698,
        "DeleteDiffCount": 3,
        "DiffFileResourceId": "yDtryUUckp9tv5kcUEdITpJ9VXDn080c",
        "Message": "",
        "Operator": "yDtGuUUckp955n9yUECLj6JusBmg10dc",
        "OriginalFileResourceId": "yDtryUUckp9tv5odUEdITpJvu1v2faCj",
        "RequestId": "s1760000134519523795",
        "Status": 2,
        "TaskId": "yDtrrUUckp94goxhUyjVZ8rSEQ0lg7vb",
        "TotalDiffCount": 12
    }
}
```

**Example 2: 查询合同对比任务结果（展示详情）**



Input: 

```
tccli ess DescribeContractComparisonTask --cli-unfold-argument  \
    --Operator.UserId yDwqbUUckp3o2rzmUxHsV0j1FlhYIKo7 \
    --TaskId yDtrrUUckp94goxhUyjVZ8rSEQ0lg7vb \
    --ShowDetail True
```

Output: 
```
{
    "Response": {
        "AddDiffCount": 7,
        "ChangeDiffCount": 2,
        "Comment": "测试备注",
        "ComparisonDetail": [
            {
                "ComparisonType": "delete",
                "ContentType": "text",
                "DiffText": "",
                "OriginText": "@huaxi"
            },
            {
                "ComparisonType": "change",
                "ContentType": "text",
                "DiffText": "完整地填写上",
                "OriginText": "请乙方务必准确、完整"
            },
            {
                "ComparisonType": "add",
                "ContentType": "text",
                "DiffText": "行贷款本息",
                "OriginText": ""
            }
        ],
        "CreateTime": 1760430451,
        "DeleteDiffCount": 3,
        "DiffFileResourceId": "yDtrDUUckp99jn93UE5rKNiyiKd4XGyQ",
        "Message": "",
        "Operator": "yDt49UUckp936q0sUx2QXTeCzkDPurYe",
        "OriginalFileResourceId": "yDtrDUUckp99jn9kUE5rKNiyseDep5Xy",
        "RequestId": "s1760430603916269519",
        "Status": 2,
        "TaskId": "yDtTFUUckp9elogcUudRpd6uv7cdx6Qa",
        "TotalDiffCount": 12
    }
}
```

