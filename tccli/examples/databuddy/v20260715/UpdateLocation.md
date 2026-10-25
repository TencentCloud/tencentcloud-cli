**Example 1: 修改存储位置信息**

修改存储位置的名称、描述或属性信息

Input: 

```
tccli databuddy UpdateLocation --cli-unfold-argument  \
    --LocationName test_1 \
    --Updates.0.UpdateType modify_location_comment \
    --Updates.0.NewComment updated comment \
    --WorkspaceId 17697667906247629
```

Output: 
```
{
    "Response": {
        "Data": {
            "Location": {
                "LocationName": "test_1",
                "LocationUri": "cos://bucket-30-251436191",
                "Comment": "updated comment"
            }
        },
        "RequestId": "ea139f3f-cbf7-46b4-8ef3-a1a99bf2b655"
    }
}
```

