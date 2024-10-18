**Example 1: 仿冒应用举报**

仿冒应用举报

Input: 

```
tccli bma CreateBPFakeAPP --cli-unfold-argument  \
    --CompanyId 123 \
    --FakeAPPName 仿冒应用名称 \
    --APPChan 仿冒来源 \
    --FakeAPPPackageName 仿冒应用包名 \
    --FakeAPPCert 仿冒应用证书 \
    --FakeAPPSize 仿冒应用大小 \
    --FakeAPPSnapshots 仿冒截图 \
    --Note 备注
```

Output: 
```
{
    "Response": {
        "FakeAPPId": 12,
        "RequestId": "xxx"
    }
}
```

