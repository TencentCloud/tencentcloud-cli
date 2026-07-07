**Example 1: 查询模型路由实例下关联模型的可用性**



Input: 

```
tccli clb DescribeAssociatedModelAvailability --cli-unfold-argument  \
    --ModelRouterId cmr-jcxor1gp \
    --Models claude-opus-4-6
```

Output: 
```
{
    "Response": {
        "ModelAvailability": [
            {
                "Model": "claude-opus-4-6",
                "Status": "Unavailable"
            }
        ],
        "RequestId": "419c98bf-e319-4c86-bbd7-fadc09c3c9a0"
    }
}
```

**Example 2: 查询模型路由实例下关联模型的可用性（文本输入可用）**

查询模型路由实例下关联模型的可用性（文本输入可用）

Input: 

```
tccli clb DescribeAssociatedModelAvailability --cli-unfold-argument  \
    --ModelRouterId cmr-pmmvy9l7 \
    --Models gpt-4o-textonly
```

Output: 
```
{
    "Response": {
        "ModelAvailability": [
            {
                "InputModalities": [
                    "text"
                ],
                "Model": "gpt-4o-textonly",
                "Status": "Available"
            }
        ],
        "RequestId": "9bff26d3-85c8-4ad6-a436-20d302fa86ba"
    }
}
```

**Example 3: 查询模型路由实例下关联模型的可用性（模型不健康导致当前无可用输入多模态能力）**

查询模型路由实例下关联模型的可用性（模型不健康导致当前无可用输入多模态能力）

Input: 

```
tccli clb DescribeAssociatedModelAvailability --cli-unfold-argument  \
    --ModelRouterId cmr-pmmvy9l7 \
    --Models gpt-4o-textonly
```

Output: 
```
{
    "Response": {
        "ModelAvailability": [
            {
                "InputModalities": [],
                "Model": "gpt-4o-textonly",
                "Status": "Unavailable"
            }
        ],
        "RequestId": "b2b48e35-aabb-479c-ab3b-d7b69562227e"
    }
}
```

