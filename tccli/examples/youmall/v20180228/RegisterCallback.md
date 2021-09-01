**Example 1: 门店到访通知回调地址注册接口 - 成功示例**



Input: 

```
tccli youmall RegisterCallback --cli-unfold-argument  \
    --CompanyId TestCompany \
    --BackUrl TestUrl \
    --Time 1529898082
```

Output: 
```
{
    "Response": {
        "RequestId": "6ec80684-0879-405e-8932-72e7c0c48ef8"
    }
}
```

**Example 2: 门店到访通知回调地址注册接口 - 失败示例**



Input: 

```
tccli youmall RegisterCallback --cli-unfold-argument  \
    --CompanyId TestCompany \
    --BackUrl TestUrl \
    --Time 1529898082
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter ",
            "Message": "参数错误"
        },
        "RequestId": "6ec80684-0879-405e-8932-72e7c0c48ef8"
    }
}
```

