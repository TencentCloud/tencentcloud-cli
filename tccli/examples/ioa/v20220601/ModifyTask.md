**Example 1: 取消任务**

取消任务

Input: 

```
tccli ioa ModifyTask --cli-unfold-argument  \
    --SeqId 27 \
    --Owner admin
```

Output: 
```
{
    "Response": {
        "Data": {
            "SeqId": 28
        },
        "RequestId": "615f8ab2-9a0d-4f6b-a022-0f6b209be1bc"
    }
}
```

