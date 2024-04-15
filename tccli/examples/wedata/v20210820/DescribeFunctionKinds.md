**Example 1: 查询函数分类**



Input: 

```
tccli wedata DescribeFunctionKinds --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Kinds": [
            {
                "EnName": "analytical functions",
                "Name": "ANALYSIS",
                "ZhName": "分析函数"
            },
            {
                "EnName": "encryption function",
                "Name": "ENCRYPTION",
                "ZhName": "加密函数"
            },
            {
                "EnName": "aggregate function",
                "Name": "AGGREGATE",
                "ZhName": "聚合函数"
            }
        ],
        "ErrorMessage": null,
        "RequestId": "87b71fd5-190f-4bea-87ad-b5c0891c74a3"
    }
}
```

