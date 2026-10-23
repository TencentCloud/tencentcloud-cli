**Example 1: 用户集成列表**



Input: 

```
tccli tcb GetUserKeyList --cli-unfold-argument  \
    --EnvId lowcode-0g2qsnk29ac7c5e8 \
    --Offset 0 \
    --Limit 50 \
    --Business integration
```

Output: 
```
{
    "Response": {
        "RequestId": "af937458-421a-11f1-a642-52802a39496a",
        "TotalCount": 5,
        "UserKeyList": [
            {
                "AuthTypeCode": "weixinpaydc",
                "AuthTypeName": "微信支付-小程序",
                "BindServiceList": {
                    "Apis": [],
                    "Mcp": [],
                    "Other": []
                },
                "DemoCodeFunctionName": "wx-pay-zg6rmxnv-demo-scfweb",
                "Description": "",
                "Ext": "{\"appId\":\"wxc1546068399a59fc\",\"merchantId\":\"1331597701\",\"merchantSerialNumber\":\"\",\"privateKey\":\"-----BEGIN PRIVATE KEY-----\\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQClXYJt6OdwTu+l\\nUoqPXUjuG8bZB3xXoqkCkQ/8zGHwv1zkFAt0Z/sGaJfdqnSx8ojoCopF+TZWlNSb\\nvCo8GoFjt2AsjJAAINwZor09QagEPhVu8NllVXXNANo8pPABNxmJb1XhWSbMD4KU\\nJqB9rH1BoeAefJU5szINjcW0Q+fOjMm8jTimxmKgts4Uwv/ZvuyAbfcLV3rLV2D0\\n3Sc/fEh7hMgNOsw1b4Sxh/F3PFVGBlr/o8cnpEUdI3GsFioPzpU4vaP8DR79IL5C\\nUITT0S82Rv84BvHZJx+/3VhWEKLqRguLhDRLj1TzBY+EI8lGSr0B1EOV+lmBjq7P\\np0oE3R0JAgMBAAECggEARObokLlJrc8GJYF2AHRjDet++DEZSz6YY1xkJ/ZVHMXv\\ng40ilLc6rhnopVD/3KFtEBpMMQm87WiICffmNTLqFM10gjtzSMpoSzo21Y5E3rer\\noJU0T/fC5M9lH32uDyORPWWpiALomoAf7XEG0DaN3kn/o1RPrUIQKfuXlBvzO2lc\\npy1uUnUUBfSnyEzmBKwtFDerXPPHCAaeDsk3siAcDnjpUsvJz3eUrCJRIyJLmEZj\\nmLbCaEqsNTm820XcNZ9XOf+di55+IXbUoAh2JJS3kfsmF7XOohinTM5HK279AaZP\\nOxurr8FzlzvTJJux0olSk93Tp/SEp8KPIA5xnd+UrQKBgQDSqB4DUWIoAHghSAOD\\n15WeCpyta0zwX9flhZhAE+7SHAEGj6J1FePzyFkUvdLLwU3RqpaQpNSr8FhlNmUV\\nc9MlpCz5c0D7RT1YLsx7xvaUFBJPO/JWekALgprSQKwrqvVmAoc9Rgr+XuNqG6Sj\\nFeModHOsWaLR8+Roqx6LvapHAwKBgQDI9a8aVb53lyxGSSypTXMBOeoUJ4QuFEIy\\noCDjufCvOfDACk07gJ5S6tx7h9V0O2s0SEUy2Ey9L1Mr1l5CHEgdTZuqy28KNavm\\nCQsPZ+6oTuOfQt8GtsyEK87KgRImctYgms0lQ4yc6955g/6nKD9CAS51VpI6tHAJ\\nzNhznRIYAwKBgQCeBOBmqsDPsvJqPMPuPWSNZfZ7nBbd5XdlQ96eipVGZR1b15kM\\n7XvOXgZ8qZwbngiK88T4Ab1KsQMOAUy4V+cWwF3ATXV8R0cqBAj9/JTxJVFKwHQb\\n7J5oQ/NxLnQ4WYi1mcXq78TFZVaAPPY2I+//Y8N1kNOzXJmE7n/+YSr/EwKBgAIH\\nqUskzpW6qzHSj2buZ1j90sV9WLJ2dey4/VwPhsTeWvY1pG4TcIX55VxCFP/lkcGn\\ncTuAP9YxYi+xLKaSTpAtNoNVJrv9qszaDoiLTjfZBCeZr1MMCajUIHSfNSW6Rztx\\nFN1pf0QehdLIaIwbtffety9sPnHlXLRco1sXnRUtAoGAcsIeHfeAWiSk+JHSUXxC\\nlB+SNa5iNzILVMjMoA/GGEv1Jge0sSt+X5iUHGZlALq4cKSkVdng0mfHNyxXfwm7\\n5HC5/PxlRyoJCcxNvYcfeDYjUQwiQSOa5HWgiikBrtqH5vJcud4LUIHn52fDkGH7\\nWIVxUod8h2A1IPSR1iUPI3s=\\n-----END PRIVATE KEY-----\",\"apiV3Key\":\"\",\"wxPayPublicKeyId\":\"PUB_KEY_ID_0113315977012026022800111946001600\",\"wxPayPublicKey\":\"-----BEGIN PUBLIC KEY-----\\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyAUBB//LAmFAQKtXS4yP\\npqSCHBmGZdSSA7cDcYbhQbAR7Qg337jMGHokJRPTErXy3kEXBm8H+peno12bii2Z\\nLo/msnvC5tVm8JA8k+qShP+BTkijQV0hz8iMQ60S/j+ZjUwirrcn4dwCKUeHeLjK\\nq9aw2bk/bRLT2TBbhpX/xUOCUScqjpKXXyrtV20lca5hsLCDVi93W9kfmwvmfFIo\\nYtcN13hOHtCs5Nh9O0dPskg/ri5ZG8HdNZv2pBYJj3sg7vu2z1fFTlz40O3xBLb2\\n3P2lKuOG+nBMBRgqrBGFGO+VBSJyLcu+0GXBe7h4qhyeL0mWGwSPqZE98pMKhpom\\ntwIDAQAB\\n-----END PUBLIC KEY-----\",\"notifyURLCallbackType\":\"system\",\"notifyURLPayURL\":\"https://wx-pay-zg6rmxnv.integration-callback.tcloudbase.com/wechatpay/order\",\"notifyURLPayResourceType\":\"function\",\"notifyURLPayResourceName\":\"wx-pay-zg6rmxnv-demo-scfweb\",\"notifyURLRefundsURL\":\"https://wx-pay-zg6rmxnv.integration-callback.tcloudbase.com/wechatpay/refund\",\"notifyURLRefundsResourceType\":\"function\",\"notifyURLRefundsResourceName\":\"wx-pay-zg6rmxnv-demo-scfweb\"}",
                "KeyID": "wx-pay-zg6rmxnv",
                "Name": "wx-pay",
                "Status": "已发布",
                "TicketID": ""
            },
            {
                "AuthTypeCode": "weixinpaydc",
                "AuthTypeName": "微信支付-小程序",
                "BindServiceList": {
                    "Apis": [],
                    "Mcp": [],
                    "Other": []
                },
                "DemoCodeFunctionName": "weixinzhichi-plldf2yz-demo-scfweb",
                "Description": "",
                "Ext": "{\"appId\":\"wxc1546068399a59fc\",\"merchantId\":\"1331597701\",\"merchantSerialNumber\":\"\",\"privateKey\":\"-----BEGIN PRIVATE KEY-----\\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQClXYJt6OdwTu+l\\nUoqPXUjuG8bZB3xXoqkCkQ/8zGHwv1zkFAt0Z/sGaJfdqnSx8ojoCopF+TZWlNSb\\nvCo8GoFjt2AsjJAAINwZor09QagEPhVu8NllVXXNANo8pPABNxmJb1XhWSbMD4KU\\nJqB9rH1BoeAefJU5szINjcW0Q+fOjMm8jTimxmKgts4Uwv/ZvuyAbfcLV3rLV2D0\\n3Sc/fEh7hMgNOsw1b4Sxh/F3PFVGBlr/o8cnpEUdI3GsFioPzpU4vaP8DR79IL5C\\nUITT0S82Rv84BvHZJx+/3VhWEKLqRguLhDRLj1TzBY+EI8lGSr0B1EOV+lmBjq7P\\np0oE3R0JAgMBAAECggEARObokLlJrc8GJYF2AHRjDet++DEZSz6YY1xkJ/ZVHMXv\\ng40ilLc6rhnopVD/3KFtEBpMMQm87WiICffmNTLqFM10gjtzSMpoSzo21Y5E3rer\\noJU0T/fC5M9lH32uDyORPWWpiALomoAf7XEG0DaN3kn/o1RPrUIQKfuXlBvzO2lc\\npy1uUnUUBfSnyEzmBKwtFDerXPPHCAaeDsk3siAcDnjpUsvJz3eUrCJRIyJLmEZj\\nmLbCaEqsNTm820XcNZ9XOf+di55+IXbUoAh2JJS3kfsmF7XOohinTM5HK279AaZP\\nOxurr8FzlzvTJJux0olSk93Tp/SEp8KPIA5xnd+UrQKBgQDSqB4DUWIoAHghSAOD\\n15WeCpyta0zwX9flhZhAE+7SHAEGj6J1FePzyFkUvdLLwU3RqpaQpNSr8FhlNmUV\\nc9MlpCz5c0D7RT1YLsx7xvaUFBJPO/JWekALgprSQKwrqvVmAoc9Rgr+XuNqG6Sj\\nFeModHOsWaLR8+Roqx6LvapHAwKBgQDI9a8aVb53lyxGSSypTXMBOeoUJ4QuFEIy\\noCDjufCvOfDACk07gJ5S6tx7h9V0O2s0SEUy2Ey9L1Mr1l5CHEgdTZuqy28KNavm\\nCQsPZ+6oTuOfQt8GtsyEK87KgRImctYgms0lQ4yc6955g/6nKD9CAS51VpI6tHAJ\\nzNhznRIYAwKBgQCeBOBmqsDPsvJqPMPuPWSNZfZ7nBbd5XdlQ96eipVGZR1b15kM\\n7XvOXgZ8qZwbngiK88T4Ab1KsQMOAUy4V+cWwF3ATXV8R0cqBAj9/JTxJVFKwHQb\\n7J5oQ/NxLnQ4WYi1mcXq78TFZVaAPPY2I+//Y8N1kNOzXJmE7n/+YSr/EwKBgAIH\\nqUskzpW6qzHSj2buZ1j90sV9WLJ2dey4/VwPhsTeWvY1pG4TcIX55VxCFP/lkcGn\\ncTuAP9YxYi+xLKaSTpAtNoNVJrv9qszaDoiLTjfZBCeZr1MMCajUIHSfNSW6Rztx\\nFN1pf0QehdLIaIwbtffety9sPnHlXLRco1sXnRUtAoGAcsIeHfeAWiSk+JHSUXxC\\nlB+SNa5iNzILVMjMoA/GGEv1Jge0sSt+X5iUHGZlALq4cKSkVdng0mfHNyxXfwm7\\n5HC5/PxlRyoJCcxNvYcfeDYjUQwiQSOa5HWgiikBrtqH5vJcud4LUIHn52fDkGH7\\nWIVxUod8h2A1IPSR1iUPI3s=\\n-----END PRIVATE KEY-----\",\"apiV3Key\":\"\",\"wxPayPublicKeyId\":\"PUB_KEY_ID_0113315977012026022800111946001600\",\"wxPayPublicKey\":\"-----BEGIN PUBLIC KEY-----\\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyAUBB//LAmFAQKtXS4yP\\npqSCHBmGZdSSA7cDcYbhQbAR7Qg337jMGHokJRPTErXy3kEXBm8H+peno12bii2Z\\nLo/msnvC5tVm8JA8k+qShP+BTkijQV0hz8iMQ60S/j+ZjUwirrcn4dwCKUeHeLjK\\nq9aw2bk/bRLT2TBbhpX/xUOCUScqjpKXXyrtV20lca5hsLCDVi93W9kfmwvmfFIo\\nYtcN13hOHtCs5Nh9O0dPskg/ri5ZG8HdNZv2pBYJj3sg7vu2z1fFTlz40O3xBLb2\\n3P2lKuOG+nBMBRgqrBGFGO+VBSJyLcu+0GXBe7h4qhyeL0mWGwSPqZE98pMKhpom\\ntwIDAQAB\\n-----END PUBLIC KEY-----\",\"notifyURLCallbackType\":\"system\",\"notifyURLPayURL\":\"https://weixinzhichi-plldf2yz.integration-callback.tcloudbase.com/wechatpay/order\",\"notifyURLPayResourceType\":\"function\",\"notifyURLPayResourceName\":\"weixinzhichi-plldf2yz-demo-scfweb\",\"notifyURLRefundsURL\":\"https://weixinzhichi-plldf2yz.integration-callback.tcloudbase.com/wechatpay/refund\",\"notifyURLRefundsResourceType\":\"function\",\"notifyURLRefundsResourceName\":\"weixinzhichi-plldf2yz-demo-scfweb\"}",
                "KeyID": "weixinzhichi-plldf2yz",
                "Name": "微信支付",
                "Status": "已发布",
                "TicketID": ""
            },
            {
                "AuthTypeCode": "weixinpaydc",
                "AuthTypeName": "微信支付-小程序",
                "BindServiceList": {
                    "Apis": [],
                    "Mcp": [],
                    "Other": []
                },
                "DemoCodeFunctionName": "wx-pay-zg6rmxnv-demo-scfweb",
                "Description": "",
                "Ext": "{\"appId\":\"wxc1546068399a59fc\",\"merchantId\":\"1331597701\",\"merchantSerialNumber\":\"\",\"privateKey\":\"-----BEGIN PRIVATE KEY-----\\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQClXYJt6OdwTu+l\\nUoqPXUjuG8bZB3xXoqkCkQ/8zGHwv1zkFAt0Z/sGaJfdqnSx8ojoCopF+TZWlNSb\\nvCo8GoFjt2AsjJAAINwZor09QagEPhVu8NllVXXNANo8pPABNxmJb1XhWSbMD4KU\\nJqB9rH1BoeAefJU5szINjcW0Q+fOjMm8jTimxmKgts4Uwv/ZvuyAbfcLV3rLV2D0\\n3Sc/fEh7hMgNOsw1b4Sxh/F3PFVGBlr/o8cnpEUdI3GsFioPzpU4vaP8DR79IL5C\\nUITT0S82Rv84BvHZJx+/3VhWEKLqRguLhDRLj1TzBY+EI8lGSr0B1EOV+lmBjq7P\\np0oE3R0JAgMBAAECggEARObokLlJrc8GJYF2AHRjDet++DEZSz6YY1xkJ/ZVHMXv\\ng40ilLc6rhnopVD/3KFtEBpMMQm87WiICffmNTLqFM10gjtzSMpoSzo21Y5E3rer\\noJU0T/fC5M9lH32uDyORPWWpiALomoAf7XEG0DaN3kn/o1RPrUIQKfuXlBvzO2lc\\npy1uUnUUBfSnyEzmBKwtFDerXPPHCAaeDsk3siAcDnjpUsvJz3eUrCJRIyJLmEZj\\nmLbCaEqsNTm820XcNZ9XOf+di55+IXbUoAh2JJS3kfsmF7XOohinTM5HK279AaZP\\nOxurr8FzlzvTJJux0olSk93Tp/SEp8KPIA5xnd+UrQKBgQDSqB4DUWIoAHghSAOD\\n15WeCpyta0zwX9flhZhAE+7SHAEGj6J1FePzyFkUvdLLwU3RqpaQpNSr8FhlNmUV\\nc9MlpCz5c0D7RT1YLsx7xvaUFBJPO/JWekALgprSQKwrqvVmAoc9Rgr+XuNqG6Sj\\nFeModHOsWaLR8+Roqx6LvapHAwKBgQDI9a8aVb53lyxGSSypTXMBOeoUJ4QuFEIy\\noCDjufCvOfDACk07gJ5S6tx7h9V0O2s0SEUy2Ey9L1Mr1l5CHEgdTZuqy28KNavm\\nCQsPZ+6oTuOfQt8GtsyEK87KgRImctYgms0lQ4yc6955g/6nKD9CAS51VpI6tHAJ\\nzNhznRIYAwKBgQCeBOBmqsDPsvJqPMPuPWSNZfZ7nBbd5XdlQ96eipVGZR1b15kM\\n7XvOXgZ8qZwbngiK88T4Ab1KsQMOAUy4V+cWwF3ATXV8R0cqBAj9/JTxJVFKwHQb\\n7J5oQ/NxLnQ4WYi1mcXq78TFZVaAPPY2I+//Y8N1kNOzXJmE7n/+YSr/EwKBgAIH\\nqUskzpW6qzHSj2buZ1j90sV9WLJ2dey4/VwPhsTeWvY1pG4TcIX55VxCFP/lkcGn\\ncTuAP9YxYi+xLKaSTpAtNoNVJrv9qszaDoiLTjfZBCeZr1MMCajUIHSfNSW6Rztx\\nFN1pf0QehdLIaIwbtffety9sPnHlXLRco1sXnRUtAoGAcsIeHfeAWiSk+JHSUXxC\\nlB+SNa5iNzILVMjMoA/GGEv1Jge0sSt+X5iUHGZlALq4cKSkVdng0mfHNyxXfwm7\\n5HC5/PxlRyoJCcxNvYcfeDYjUQwiQSOa5HWgiikBrtqH5vJcud4LUIHn52fDkGH7\\nWIVxUod8h2A1IPSR1iUPI3s=\\n-----END PRIVATE KEY-----\",\"apiV3Key\":\"\",\"wxPayPublicKeyId\":\"PUB_KEY_ID_0113315977012026022800111946001600\",\"wxPayPublicKey\":\"-----BEGIN PUBLIC KEY-----\\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyAUBB//LAmFAQKtXS4yP\\npqSCHBmGZdSSA7cDcYbhQbAR7Qg337jMGHokJRPTErXy3kEXBm8H+peno12bii2Z\\nLo/msnvC5tVm8JA8k+qShP+BTkijQV0hz8iMQ60S/j+ZjUwirrcn4dwCKUeHeLjK\\nq9aw2bk/bRLT2TBbhpX/xUOCUScqjpKXXyrtV20lca5hsLCDVi93W9kfmwvmfFIo\\nYtcN13hOHtCs5Nh9O0dPskg/ri5ZG8HdNZv2pBYJj3sg7vu2z1fFTlz40O3xBLb2\\n3P2lKuOG+nBMBRgqrBGFGO+VBSJyLcu+0GXBe7h4qhyeL0mWGwSPqZE98pMKhpom\\ntwIDAQAB\\n-----END PUBLIC KEY-----\",\"notifyURLCallbackType\":\"system\",\"notifyURLPayURL\":\"https://wx-pay-zg6rmxnv1.integration-callback.tcloudbase.com/wechatpay/order\",\"notifyURLPayResourceType\":\"function\",\"notifyURLPayResourceName\":\"wx-pay-zg6rmxnv1-demo-scfweb\",\"notifyURLRefundsURL\":\"https://wx-pay-zg6rmxnv1.integration-callback.tcloudbase.com/wechatpay/refund\",\"notifyURLRefundsResourceType\":\"function\",\"notifyURLRefundsResourceName\":\"wx-pay-zg6rmxnv1-demo-scfweb\"}",
                "KeyID": "wx-pay-zg6rmxnv1",
                "Name": "wx-pay",
                "Status": "已发布",
                "TicketID": ""
            },
            {
                "AuthTypeCode": "weixinpaydc",
                "AuthTypeName": "微信支付-小程序",
                "BindServiceList": {
                    "Apis": [],
                    "Mcp": [],
                    "Other": []
                },
                "DemoCodeFunctionName": "wx-pay-zg6rmxnv-demo-scfweb",
                "Description": "",
                "Ext": "{\"appId\":\"wxc1546068399a59fc\",\"merchantId\":\"1331597701\",\"merchantSerialNumber\":\"\",\"privateKey\":\"-----BEGIN PRIVATE KEY-----\\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQClXYJt6OdwTu+l\\nUoqPXUjuG8bZB3xXoqkCkQ/8zGHwv1zkFAt0Z/sGaJfdqnSx8ojoCopF+TZWlNSb\\nvCo8GoFjt2AsjJAAINwZor09QagEPhVu8NllVXXNANo8pPABNxmJb1XhWSbMD4KU\\nJqB9rH1BoeAefJU5szINjcW0Q+fOjMm8jTimxmKgts4Uwv/ZvuyAbfcLV3rLV2D0\\n3Sc/fEh7hMgNOsw1b4Sxh/F3PFVGBlr/o8cnpEUdI3GsFioPzpU4vaP8DR79IL5C\\nUITT0S82Rv84BvHZJx+/3VhWEKLqRguLhDRLj1TzBY+EI8lGSr0B1EOV+lmBjq7P\\np0oE3R0JAgMBAAECggEARObokLlJrc8GJYF2AHRjDet++DEZSz6YY1xkJ/ZVHMXv\\ng40ilLc6rhnopVD/3KFtEBpMMQm87WiICffmNTLqFM10gjtzSMpoSzo21Y5E3rer\\noJU0T/fC5M9lH32uDyORPWWpiALomoAf7XEG0DaN3kn/o1RPrUIQKfuXlBvzO2lc\\npy1uUnUUBfSnyEzmBKwtFDerXPPHCAaeDsk3siAcDnjpUsvJz3eUrCJRIyJLmEZj\\nmLbCaEqsNTm820XcNZ9XOf+di55+IXbUoAh2JJS3kfsmF7XOohinTM5HK279AaZP\\nOxurr8FzlzvTJJux0olSk93Tp/SEp8KPIA5xnd+UrQKBgQDSqB4DUWIoAHghSAOD\\n15WeCpyta0zwX9flhZhAE+7SHAEGj6J1FePzyFkUvdLLwU3RqpaQpNSr8FhlNmUV\\nc9MlpCz5c0D7RT1YLsx7xvaUFBJPO/JWekALgprSQKwrqvVmAoc9Rgr+XuNqG6Sj\\nFeModHOsWaLR8+Roqx6LvapHAwKBgQDI9a8aVb53lyxGSSypTXMBOeoUJ4QuFEIy\\noCDjufCvOfDACk07gJ5S6tx7h9V0O2s0SEUy2Ey9L1Mr1l5CHEgdTZuqy28KNavm\\nCQsPZ+6oTuOfQt8GtsyEK87KgRImctYgms0lQ4yc6955g/6nKD9CAS51VpI6tHAJ\\nzNhznRIYAwKBgQCeBOBmqsDPsvJqPMPuPWSNZfZ7nBbd5XdlQ96eipVGZR1b15kM\\n7XvOXgZ8qZwbngiK88T4Ab1KsQMOAUy4V+cWwF3ATXV8R0cqBAj9/JTxJVFKwHQb\\n7J5oQ/NxLnQ4WYi1mcXq78TFZVaAPPY2I+//Y8N1kNOzXJmE7n/+YSr/EwKBgAIH\\nqUskzpW6qzHSj2buZ1j90sV9WLJ2dey4/VwPhsTeWvY1pG4TcIX55VxCFP/lkcGn\\ncTuAP9YxYi+xLKaSTpAtNoNVJrv9qszaDoiLTjfZBCeZr1MMCajUIHSfNSW6Rztx\\nFN1pf0QehdLIaIwbtffety9sPnHlXLRco1sXnRUtAoGAcsIeHfeAWiSk+JHSUXxC\\nlB+SNa5iNzILVMjMoA/GGEv1Jge0sSt+X5iUHGZlALq4cKSkVdng0mfHNyxXfwm7\\n5HC5/PxlRyoJCcxNvYcfeDYjUQwiQSOa5HWgiikBrtqH5vJcud4LUIHn52fDkGH7\\nWIVxUod8h2A1IPSR1iUPI3s=\\n-----END PRIVATE KEY-----\",\"apiV3Key\":\"\",\"wxPayPublicKeyId\":\"PUB_KEY_ID_0113315977012026022800111946001600\",\"wxPayPublicKey\":\"-----BEGIN PUBLIC KEY-----\\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyAUBB//LAmFAQKtXS4yP\\npqSCHBmGZdSSA7cDcYbhQbAR7Qg337jMGHokJRPTErXy3kEXBm8H+peno12bii2Z\\nLo/msnvC5tVm8JA8k+qShP+BTkijQV0hz8iMQ60S/j+ZjUwirrcn4dwCKUeHeLjK\\nq9aw2bk/bRLT2TBbhpX/xUOCUScqjpKXXyrtV20lca5hsLCDVi93W9kfmwvmfFIo\\nYtcN13hOHtCs5Nh9O0dPskg/ri5ZG8HdNZv2pBYJj3sg7vu2z1fFTlz40O3xBLb2\\n3P2lKuOG+nBMBRgqrBGFGO+VBSJyLcu+0GXBe7h4qhyeL0mWGwSPqZE98pMKhpom\\ntwIDAQAB\\n-----END PUBLIC KEY-----\",\"notifyURLCallbackType\":\"system\",\"notifyURLPayURL\":\"https://wx-pay-zg6rmxnv2.integration-callback.tcloudbase.com/wechatpay/order\",\"notifyURLPayResourceType\":\"function\",\"notifyURLPayResourceName\":\"wx-pay-zg6rmxnv2-demo-scfweb\",\"notifyURLRefundsURL\":\"https://wx-pay-zg6rmxnv2.integration-callback.tcloudbase.com/wechatpay/refund\",\"notifyURLRefundsResourceType\":\"function\",\"notifyURLRefundsResourceName\":\"wx-pay-zg6rmxnv2-demo-scfweb\"}",
                "KeyID": "wx-pay-zg6rmxnv2",
                "Name": "wx-pay",
                "Status": "已发布",
                "TicketID": ""
            },
            {
                "AuthTypeCode": "weixinpaydc",
                "AuthTypeName": "微信支付-小程序",
                "BindServiceList": {
                    "Apis": [],
                    "Mcp": [],
                    "Other": []
                },
                "DemoCodeFunctionName": "wx-pay-zg6rmxnv-demo-scfweb",
                "Description": "",
                "Ext": "{\"appId\":\"wxc1546068399a59fc\",\"merchantId\":\"1331597701\",\"merchantSerialNumber\":\"\",\"privateKey\":\"-----BEGIN PRIVATE KEY-----\\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQClXYJt6OdwTu+l\\nUoqPXUjuG8bZB3xXoqkCkQ/8zGHwv1zkFAt0Z/sGaJfdqnSx8ojoCopF+TZWlNSb\\nvCo8GoFjt2AsjJAAINwZor09QagEPhVu8NllVXXNANo8pPABNxmJb1XhWSbMD4KU\\nJqB9rH1BoeAefJU5szINjcW0Q+fOjMm8jTimxmKgts4Uwv/ZvuyAbfcLV3rLV2D0\\n3Sc/fEh7hMgNOsw1b4Sxh/F3PFVGBlr/o8cnpEUdI3GsFioPzpU4vaP8DR79IL5C\\nUITT0S82Rv84BvHZJx+/3VhWEKLqRguLhDRLj1TzBY+EI8lGSr0B1EOV+lmBjq7P\\np0oE3R0JAgMBAAECggEARObokLlJrc8GJYF2AHRjDet++DEZSz6YY1xkJ/ZVHMXv\\ng40ilLc6rhnopVD/3KFtEBpMMQm87WiICffmNTLqFM10gjtzSMpoSzo21Y5E3rer\\noJU0T/fC5M9lH32uDyORPWWpiALomoAf7XEG0DaN3kn/o1RPrUIQKfuXlBvzO2lc\\npy1uUnUUBfSnyEzmBKwtFDerXPPHCAaeDsk3siAcDnjpUsvJz3eUrCJRIyJLmEZj\\nmLbCaEqsNTm820XcNZ9XOf+di55+IXbUoAh2JJS3kfsmF7XOohinTM5HK279AaZP\\nOxurr8FzlzvTJJux0olSk93Tp/SEp8KPIA5xnd+UrQKBgQDSqB4DUWIoAHghSAOD\\n15WeCpyta0zwX9flhZhAE+7SHAEGj6J1FePzyFkUvdLLwU3RqpaQpNSr8FhlNmUV\\nc9MlpCz5c0D7RT1YLsx7xvaUFBJPO/JWekALgprSQKwrqvVmAoc9Rgr+XuNqG6Sj\\nFeModHOsWaLR8+Roqx6LvapHAwKBgQDI9a8aVb53lyxGSSypTXMBOeoUJ4QuFEIy\\noCDjufCvOfDACk07gJ5S6tx7h9V0O2s0SEUy2Ey9L1Mr1l5CHEgdTZuqy28KNavm\\nCQsPZ+6oTuOfQt8GtsyEK87KgRImctYgms0lQ4yc6955g/6nKD9CAS51VpI6tHAJ\\nzNhznRIYAwKBgQCeBOBmqsDPsvJqPMPuPWSNZfZ7nBbd5XdlQ96eipVGZR1b15kM\\n7XvOXgZ8qZwbngiK88T4Ab1KsQMOAUy4V+cWwF3ATXV8R0cqBAj9/JTxJVFKwHQb\\n7J5oQ/NxLnQ4WYi1mcXq78TFZVaAPPY2I+//Y8N1kNOzXJmE7n/+YSr/EwKBgAIH\\nqUskzpW6qzHSj2buZ1j90sV9WLJ2dey4/VwPhsTeWvY1pG4TcIX55VxCFP/lkcGn\\ncTuAP9YxYi+xLKaSTpAtNoNVJrv9qszaDoiLTjfZBCeZr1MMCajUIHSfNSW6Rztx\\nFN1pf0QehdLIaIwbtffety9sPnHlXLRco1sXnRUtAoGAcsIeHfeAWiSk+JHSUXxC\\nlB+SNa5iNzILVMjMoA/GGEv1Jge0sSt+X5iUHGZlALq4cKSkVdng0mfHNyxXfwm7\\n5HC5/PxlRyoJCcxNvYcfeDYjUQwiQSOa5HWgiikBrtqH5vJcud4LUIHn52fDkGH7\\nWIVxUod8h2A1IPSR1iUPI3s=\\n-----END PRIVATE KEY-----\",\"apiV3Key\":\"\",\"wxPayPublicKeyId\":\"PUB_KEY_ID_0113315977012026022800111946001600\",\"wxPayPublicKey\":\"-----BEGIN PUBLIC KEY-----\\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyAUBB//LAmFAQKtXS4yP\\npqSCHBmGZdSSA7cDcYbhQbAR7Qg337jMGHokJRPTErXy3kEXBm8H+peno12bii2Z\\nLo/msnvC5tVm8JA8k+qShP+BTkijQV0hz8iMQ60S/j+ZjUwirrcn4dwCKUeHeLjK\\nq9aw2bk/bRLT2TBbhpX/xUOCUScqjpKXXyrtV20lca5hsLCDVi93W9kfmwvmfFIo\\nYtcN13hOHtCs5Nh9O0dPskg/ri5ZG8HdNZv2pBYJj3sg7vu2z1fFTlz40O3xBLb2\\n3P2lKuOG+nBMBRgqrBGFGO+VBSJyLcu+0GXBe7h4qhyeL0mWGwSPqZE98pMKhpom\\ntwIDAQAB\\n-----END PUBLIC KEY-----\",\"notifyURLCallbackType\":\"system\",\"notifyURLPayURL\":\"https://wx-pay-zg6rmxnv3.integration-callback.tcloudbase.com/wechatpay/order\",\"notifyURLPayResourceType\":\"function\",\"notifyURLPayResourceName\":\"wx-pay-zg6rmxnv3-demo-scfweb\",\"notifyURLRefundsURL\":\"https://wx-pay-zg6rmxnv3.integration-callback.tcloudbase.com/wechatpay/refund\",\"notifyURLRefundsResourceType\":\"function\",\"notifyURLRefundsResourceName\":\"wx-pay-zg6rmxnv3-demo-scfweb\"}",
                "KeyID": "wx-pay-zg6rmxnv3",
                "Name": "wx-pay",
                "Status": "已发布",
                "TicketID": ""
            }
        ]
    }
}
```

