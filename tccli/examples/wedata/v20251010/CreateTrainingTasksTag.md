**Example 1: 添加运行任务标签不存在失败**



Input: 

```
tccli wedata CreateTrainingTasksTag --cli-unfold-argument  \
    --WorkspaceId 10086 \
    --RunIds 1 \
    --Key key1 \
    --Value key2
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "ResourceNotFound.MlflowResourceNotFound",
            "Message": "错误代码:[1305101], 错误描述:[Mlflow资源未找到，错误详情：Run with id=1 not found]"
        },
        "RequestId": "4e85f4b9-424c-408e-99cb-3473c8ffdb44"
    }
}
```

**Example 2: 添加运行任务标签成功**



Input: 

```
tccli wedata CreateTrainingTasksTag --cli-unfold-argument  \
    --WorkspaceId 10086 \
    --RunIds 5381d7a1ff16486484a35eeac29aa6b0 \
    --Key key1 \
    --Value key2
```

Output: 
```
{
    "Response": {
        "Data": {
            "Results": [
                {
                    "RunId": "5381d7a1ff16486484a35eeac29aa6b0",
                    "Status": true
                }
            ]
        },
        "RequestId": "90b6c1fe-3ef7-4666-a38e-6a6705431d4b"
    }
}
```

