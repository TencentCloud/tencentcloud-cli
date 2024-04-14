**Example 1: 查询规则模板维度分布情况**

查询规则模板维度分布情况

Input: 

```
tccli wedata DescribeTemplateDimCount --cli-unfold-argument  \
    --ProjectId 155477816857664 \
    --Type 1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Count": 40,
                "QualityDim": 1
            },
            {
                "Count": 4,
                "QualityDim": 2
            },
            {
                "Count": 2,
                "QualityDim": 3
            },
            {
                "Count": 3,
                "QualityDim": 4
            },
            {
                "Count": 1,
                "QualityDim": 5
            },
            {
                "Count": 6,
                "QualityDim": 6
            }
        ],
        "RequestId": "09b57279-131e-48b5-b918-1969f5d7cf5a"
    }
}
```

