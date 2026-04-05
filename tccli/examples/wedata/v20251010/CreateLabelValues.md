**Example 1: 创建标签值**

创建标签值

Input: 

```
tccli wedata CreateLabelValues --cli-unfold-argument  \
    --LabelId 27 \
    --Values.0.Value labelvalue2
```

Output: 
```
{
    "Response": {
        "Data": {
            "Message": "创建成功",
            "ValueIds": [
                "54"
            ]
        },
        "RequestId": "9d6e5943-a2a8-4c8d-928f-cb8b74e08178"
    }
}
```

