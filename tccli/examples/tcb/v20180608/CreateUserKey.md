**Example 1: 创建微信支付集成**



Input: 

```
tccli tcb CreateUserKey --cli-unfold-argument  \
    --EnvId lowcode-0g2qsnk29ac7c5e8 \
    --Name wx-pay \
    --KeyID wx-pay-zg6rmxnv3 \
    --AuthTypeCode weixinpaydc \
    --Ext {"notifyURLCallbackType":"system","notifyURLPayResourceType":"function","notifyURLRefundsResourceType":"function","notifyURLPayURL":"https://wx-pay-zg6rmxnv3.integration-callback.tcloudbase.com/wechatpay/order","notifyURLRefundsURL":"https://wx-pay-zg6rmxnv3.integration-callback.tcloudbase.com/wechatpay/refund","notifyURLPayResourceName":"wx-pay-zg6rmxnv3-demo-scfweb","notifyURLRefundsResourceName":"wx-pay-zg6rmxnv3-demo-scfweb","type":2,"appId":"xxx","merchantId":"xxx","merchantSerialNumber":"xxx==vaU3a0fK1G/JUsTzLkBYHGoKpzYStJr43HGa6BG+xxx","privateKey":"-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQClXYJt6OdwTu+l\xxxxx\n5HC5/PxlRyoJCcxNvYcfeDYjUQwiQSOa5HWgiikBrtqH5vJcud4LUIHn52fDkGH7\nWIVxUod8h2A1IPSR1iUPI3s=\n-----END PRIVATE KEY-----","apiV3Key":"vUZgkXeA7rJo6CMi3q5Psw==+39rYyVvCXD+UvmvDcGj26S6WMy+ifrKNvCWcuZrhxSOLMvxor/FI/P12REOItsN","wxPayPublicKeyId":"PUB_KEY_ID_0113315977012026022800111946001600","wxPayPublicKey":"-----BEGIN PUBLIC KEY-----\nxxxLb2\n3P2lKuOG+nBMBRgqrBGFGO+VBSJyLcu+0GXBe7h4qhyeL0mWGwSPqZE98pMKhpom\ntwIDAQAB\n-----END PUBLIC KEY-----"} \
    --Business integration \
    --DemoCodeFunctionName wx-pay-zg6rmxnv-demo-scfweb \
    --RuntimeConfig.Runtime Nodejs18.15 \
    --RuntimeConfig.MemorySize 256 \
    --RuntimeConfig.InstallDependency True \
    --RuntimeConfig.Timeout 900 \
    --RuntimeConfig.Code.CosBucketRegion ap-shanghai \
    --RuntimeConfig.Code.TempCosObjectName /2026-04-23/1259548930/lowcode-0g2qsnk29ac7c5e8/wx-pay-zg6rmxnv-demo-scfweb.zip
```

Output: 
```
{
    "Response": {
        "CreateResult": 1,
        "RequestId": "9148111c-909d-42e5-a490-6e5d5869e044"
    }
}
```

