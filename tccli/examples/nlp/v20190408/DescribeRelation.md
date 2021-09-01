**Example 1: 实体关系查询**

给定两个实体的名称，查询两个实体的边关系。常用于个性化推荐、搜索，智能问答等业务场景。

Input: 

```
tccli nlp DescribeRelation --cli-unfold-argument  \
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
                            "6b989d08-ecc5-4695-8857-5a5780c7bda1"
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
                            "b7d24d73-621a-4fdc-af5b-0c6e69a2c12f"
                        ],
                        "Name": [
                            "广东"
                        ],
                        "Popular": [
                            902
                        ]
                    }
                ]
            },
            {
                "Object": [
                    {
                        "Id": [
                            "6b989d08-ecc5-4695-8857-5a5780c7bda1"
                        ],
                        "Name": [
                            "深圳"
                        ],
                        "Popular": [
                            900
                        ]
                    }
                ],
                "Relation": "相关实体",
                "Subject": [
                    {
                        "Id": [
                            "b7d24d73-621a-4fdc-af5b-0c6e69a2c12f"
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
        "RequestId": "0e113f49-853d-4ab1-af86-f504a47c68a1"
    }
}
```

