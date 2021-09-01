**Example 1: 实体关系查询**

给定两个实体的名称，查询两个实体的边关系。常用于个性化推荐、搜索，智能问答等业务场景。

Input: 

```
tccli tkgdq DescribeRelation --cli-unfold-argument  \
    --LeftEntityName 广东省 \
    --RightEntityName 深圳市
```

Output: 
```
{
    "Response": {
        "Content": [
            {
                "Object": [
                    {
                        "Id": [
                            "7650581563784668161"
                        ],
                        "Name": [
                            "深圳"
                        ],
                        "Popular": [
                            900
                        ]
                    }
                ],
                "Relation": "下辖地区",
                "Subject": [
                    {
                        "Id": [
                            "4155123354574173272"
                        ],
                        "Name": [
                            "广东"
                        ],
                        "Popular": [
                            902
                        ]
                    }
                ]
            }
        ],
        "RequestId": "a56c90ba-167e-4ff0-9170-e44d6894e192"
    }
}
```

