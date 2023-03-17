**Example 1: 为资源关联项目**

为资源关联项目。

Input: 

```
tccli tag AttachResourceProject --cli-unfold-argument  \
    --ProjectId 1 \
    --Resource qcs::cvm:ap-beijing:uin/1234567:instance/ins-123
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-xxxxx"
    }
}
```

