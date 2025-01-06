**Example 1: 修改属性标签**

修改属性标签

Input: 

```
tccli lkeap ModifyAttributeLabel --cli-unfold-argument  \
    --Labels.0.LabelId 1830993312978765760 \
    --Labels.0.LabelName 主流 \
    --Labels.1.LabelId 1830993312978765761 \
    --Labels.1.LabelName 现代
```

Output: 
```
{
    "Response": {
        "RequestId": "04ba0a85-161a-408a-9c80-029601af9775"
    }
}
```

