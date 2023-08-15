**Example 1: 暂停指定域名的解析**



Input: 

```
tccli gaap DisableGlobalDomain --cli-unfold-argument  \
    --DomainId test.com
```

Output: 
```
{
    "Response": {
        "RequestId": "d5fc71eb-451a-40f2-933f-2732c8990d7f",
        "Error": {
            "Message": "domain not exits",
            "Code": "FailedOperation"
        }
    }
}
```

