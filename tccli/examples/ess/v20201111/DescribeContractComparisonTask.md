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

