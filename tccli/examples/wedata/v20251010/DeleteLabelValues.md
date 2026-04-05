**Example 1: 删除标签值**

删除标签值

Input: 

```
tccli wedata DeleteLabelValues --cli-unfold-argument  \
    --LabelId 27 \
    --Values 53
```

Output: 
```
{
    "Response": {
        "Data": {
            "DeletedCount": 0,
            "Message": "删除成功"
        },
        "RequestId": "ce30866d-9e09-463a-a3e8-86d096346dce"
    }
}
```

