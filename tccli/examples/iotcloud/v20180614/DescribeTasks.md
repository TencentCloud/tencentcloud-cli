**Example 1: 获取任务列表**



Input: 

```
tccli iotcloud DescribeTasks --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Tasks": [
            {
                "Type": "PublishMessage",
                "Id": "5ad5b9a53332ea3de678ea52",
                "ProductId": "ABCDE12345",
                "Status": 3,
                "CreateTime": 1523956133,
                "UpdateTime": 1523958284,
                "RetCode": 0,
                "ErrMsg": ""
            }
        ],
        "RequestId": "xxxxxxxxxxxxxxxxxxxxxxx"
    }
}
```

