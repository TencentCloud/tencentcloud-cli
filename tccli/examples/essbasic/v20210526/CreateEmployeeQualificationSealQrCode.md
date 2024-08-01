**Example 1: 生成员工执业章授权二维码**

企业需要员工授权执业章使用权限给企业时，调用接口产生二维码

Input: 

```
tccli essbasic CreateEmployeeQualificationSealQrCode --cli-unfold-argument  \
    --Agent.AppId yDwfwUUgygormhg1UuS2eARxjMT0mxAw \
    --Agent.ProxyOrganizationOpenId org_zhangsan \
    --Agent.ProxyOperator.OpenId n02468 \
    --HintText 我是提示文字
```

Output: 
```
{
    "Response": {
        "QrcodeBase64": "/9j/2wCEAAEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQ（剩余的其他图片base64字符串省略）",
        "RequestId": "5e94bc41-4767-4e98-943d-b9a455499847"
    }
}
```

