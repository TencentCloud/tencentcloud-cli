**Example 1: 验证报告盖章成功**

验证报告盖章成功

Input: 

```
tccli ca CreateVerifyReport --cli-unfold-argument  \
    --ApplyCustomerType 1 \
    --ApplyCustomerName 王五 \
    --ApplyName 经办人姓名 \
    --ApplyMobile 187****6446 \
    --FileId 70c2a5eaf142****aa12e81e7b03b637 \
    --ApplyEmail 969737738@qq.com
```

Output: 
```
{
    "Response": {
        "Code": "0",
        "Message": "2024-09-20 20:49:14 签章请求接收成功。",
        "RequestId": "67af6833-fbb6-462f-a64f-90757d68669f",
        "SignatureId": "695128****98250752"
    }
}
```

**Example 2: CreateVerifyReport**

创建验签报告

Input: 

```
tccli ca CreateVerifyReport --cli-unfold-argument  \
    --ApplyCustomerType 1 \
    --ApplyCustomerName 李四 \
    --ApplyName 王五 \
    --ApplyMobile 187****6446 \
    --FileId 27a130c8336b****865a0d251ef129b4
```

Output: 
```
{
    "Response": {
        "Code": "0",
        "Message": "签章请求接收成功",
        "RequestId": "b5d694f0-8a91-4bdc-a40d-2767b4ce8471",
        "SignatureId": "692175****51854336"
    }
}
```

