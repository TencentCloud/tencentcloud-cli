**Example 1: 查询环境统计信息列表**

查询环境统计信息列表。

Input: 

```
tccli omics DescribeEnvironmentStatistics --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "ba39197f-07d2-417b-9dfc-d8eff19a7cb0",
        "Statistics": [
            {
                "Region": "ap-guangzhou",
                "TotalCount": 10
            },
            {
                "Region": "ap-shanghai",
                "TotalCount": 0
            },
            {
                "Region": "ap-beijing",
                "TotalCount": 0
            }
        ]
    }
}
```

