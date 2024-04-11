**Example 1: 检查知识标签是否存在**

检查知识标签是否存在

Input: 

```
tccli lke CheckAttributeLabelExist --cli-unfold-argument  \
    --BotBizId 1696822786072117248 \
    --LabelName 属性修改 \
    --AttributeBizId 208 \
    --LastLabelBizId 204
```

Output: 
```
{
    "Response": {
        "IsExist": false,
        "RequestId": "7e2305f5-b348-46e2-a90a-79ebae135103"
    }
}
```

