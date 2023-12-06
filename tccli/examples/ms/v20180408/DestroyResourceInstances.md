**Example 1: 销毁资源**

销毁资源

Input: 

```
tccli ms DestroyResourceInstances --cli-unfold-argument  \
    --ResourceId 20231204_*****_0 \
    --AppPkgName com.****
```

Output: 
```
{
    "Response": {
        "OrderType": 2,
        "PlatformType": 1,
        "RequestId": "50d9287c-0d10-****",
        "ResourceId": "20231204_*****_0",
        "Result": "ok"
    }
}
```

**Example 2: 销毁资源：请求找不到资源**

销毁资源：请求找不到资源

Input: 

```
tccli ms DestroyResourceInstances --cli-unfold-argument  \
    --ResourceId 20231204_****_0 \
    --AppPkgName com.**
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "ResourceNotFound",
            "Message": "资源不存在。"
        },
        "RequestId": "62978335-*****"
    }
}
```

