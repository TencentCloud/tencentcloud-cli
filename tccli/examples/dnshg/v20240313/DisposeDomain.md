**Example 1: 下发封禁**

下发封禁

Input: 

```
tccli dnshg DisposeDomain --cli-unfold-argument  \
    --DisposeType 1 \
    --DomainList.0.Domain wwww.young49.cn \
    --DisposeWay 3 \
    --Reason 11
```

Output: 
```
{
    "Response": {
        "CommandId": "cid-fnkKvSgK1L",
        "RequestId": "b72f61fe-5ca8-4b7f-aef0-381165f2b3dd"
    }
}
```

**Example 2: 错误实例**

错误实例

Input: 

```
tccli dnshg DisposeDomain --cli-unfold-argument  \
    --DisposeType 1 \
    --DomainList.0.Domain a.com \
    --DisposeWay 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InternalError",
            "Message": "内部服务错误，请稍后重试。"
        },
        "RequestId": "14b5167d-fd84-4a3e-9cd1-debe9982ff44"
    }
}
```

