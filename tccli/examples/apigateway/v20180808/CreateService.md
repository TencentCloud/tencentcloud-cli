**Example 1: CreateService**



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
        "CreatedTime": "2018-10-30T04:24:19Z",
        "NetTypes": [
            "OUTER"
        ],
        "RequestId": "e3705d00-bfe0-4fde-942c-cebd6b12431b"
    }
}
```

