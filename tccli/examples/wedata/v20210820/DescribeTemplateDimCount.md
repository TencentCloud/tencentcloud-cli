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
                "DimType": 1,
                "Count": 1,
                "QualityDim": 1
            }
        ],
        "RequestId": "abc"
    }
}
```

