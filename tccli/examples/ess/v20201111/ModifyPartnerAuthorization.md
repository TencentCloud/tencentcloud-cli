**Example 1: 修改他方企业授权的第三方应用配置，仅能修改回调地址和key**



Input: 

```
tccli ess ModifyPartnerAuthorization --cli-unfold-argument  \
    --Operator.UserId yDwf3U*c*p*8dv**UE*******pMfa0uw \
    --BusinessId jdyxk \
    --PartnerApplicationId yD3nh****pf*u*k*******BN50TJsNwY \
    --ApplicationInfo.CallbackUrl https://v.qq.com \
    --ApplicationInfo.CallbackKey yDxjsU**yd**3*5*U********ko0F1BB
```

Output: 
```
{
    "Response": {
        "RequestId": "a0fbfba2-fb8f-43d9-bc74-87a0a63bda0a"
    }
}
```

