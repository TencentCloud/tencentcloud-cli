**Example 1: 仿冒网址举报**

仿冒网址举报

Input: 

```
tccli bma CreateBPFakeURL --cli-unfold-argument  \
    --CompanyId 123 \
    --FakeURL 举报网址 \
    --FakeURLSnapshots 仿冒截图 \
    --Note 备注
```

Output: 
```
{
    "Response": {
        "FakeURLId": 1,
        "RequestId": "xxx"
    }
}
```

