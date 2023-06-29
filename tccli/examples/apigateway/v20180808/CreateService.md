**Example 1: CreateService**

创建服务时使用

Input: 

```
tccli apigateway CreateService --cli-unfold-argument  \
    --ServiceName test_https \
    --ServiceDesc https \
    --Protocol https
```

Output: 
```
{
    "Response": {
        "ServiceId": "service-0c96l2bo",
        "ServiceName": "test_https",
        "ServiceDesc": "https",
        "OuterSubDomain": "service-0c96l2bo-1251006373.ap-guangzhou.apigateway.myqcloud.com",
        "InnerSubDomain": "",
        "IpVersion": "IPv4",
        "CreatedTime": "2020-09-22T00:00:00+00:00",
        "NetTypes": [
            "OUTER"
        ],
        "RequestId": "e3705d00-bfe0-4fde-942c-cebd6b12431b"
    }
}
```

