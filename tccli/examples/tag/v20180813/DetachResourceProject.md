**Example 1: 解绑资源和项目的关联关系**

解绑资源和项目的关联关系。

Input: 

```
tccli tag DetachResourceProject --cli-unfold-argument  \
    --ProjectId 10001 \
    --Resource qcs::cvm:ap-beijing:uin/1234567:instance/ins-123
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877dxxxxx"
    }
}
```

