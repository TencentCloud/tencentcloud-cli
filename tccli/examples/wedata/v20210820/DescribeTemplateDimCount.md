**Example 1: 查询规则模版维度分布情况**

查询规则模版维度分布情况

Input: 

```
tccli wedata DescribeTemplateDimCount --cli-unfold-argument  \
    --Type 1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Count": 1,
                "DimType": 1
            }
        ],
        "RequestId": "xx"
    }
}
```

