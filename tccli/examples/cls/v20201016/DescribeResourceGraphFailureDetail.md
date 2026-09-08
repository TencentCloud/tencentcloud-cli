**Example 1: success**



Input: 

```
tccli cls DescribeResourceGraphFailureDetail --cli-unfold-argument  \
    --ResourceGraphId 5c4efe6f-84f3-4595-aafb-92a944411f42
```

Output: 
```
{
    "Response": {
        "ErrorMessage": "topicmgr: create logset graph-logset-5c4efe6f-84f3-4595-aafb-92a944411f42: [TencentCloudSDKError] Code=ClientError.NetworkError, Message=Fail to get response because Post \"https://cls.pre.tencentcloudapi.com/\": tls: failed to verify certificate: x509: certificate is valid for tencentcloudapi.com, *.ai.ap-bangkok.tencentcloudapi.cn, *.ai.ap-bangkok.tencentcloudapi.com, *.ai.ap-bangkok.tencentcloudapi.com.cn, *.ai.ap-beijing-fsi.tencentcloudapi.cn, *.ai.ap-beijing-fsi.tencentcloudapi.com, *.ai.ap-beijing-fsi.tencentcloudapi.com.cn, *.ai.ap-beijing.tencentcloudapi.cn, *.ai.ap-beijing.tencentcloudapi.com, *.ai.ap-beijing.tencentcloudapi.com.cn, *.ai.ap-chengdu.tencentcloudapi.cn, *.ai.ap-chengdu.tencentcloudapi.com, *.ai.ap-chengdu.tencentcloudapi.com.cn, *.ai.ap-chongqing.tencentcloudapi.cn, *.ai.ap-chongqing.tencentcloudapi.com, *.ai.ap-chongqing.tencentcloudapi.com.cn, *.ai.ap-guangzhou.tencentcloudapi.cn, *.ai.ap-guangzhou.tencentcloudapi.com, *.ai.ap-guangzhou.tencentcloudapi.com.cn, *.ai.ap-hongkong.tencentcloudapi.cn, *.ai.ap-hongkong.tencentcloudapi.com, *.ai.ap-hongkong.tencentcloudapi.com.cn, *.ai.ap-jakarta.tencentcloudapi.cn, *.ai.ap-jakarta.tencentcloudapi.com, *.ai.ap-jakarta.tencentcloudapi.com.cn, *.ai.ap-mumbai.tencentcloudapi.cn, *.ai.ap-mumbai.tencentcloudapi.com, *.ai.ap-mumbai.tencentcloudapi.com.cn, *.ai.ap-nanjing.tencentcloudapi.cn, *.ai.ap-nanjing.tencentcloudapi.com, *.ai.ap-nanjing.tencentcloudapi.com.cn, *.ai.ap-seoul.tencentcloudapi.cn, *.ai.ap-seoul.tencentcloudapi.com, *.ai.ap-seoul.tencentcloudapi.com.cn, *.ai.ap-shanghai-fsi.tencentcloudapi.cn, *.ai.ap-shanghai-fsi.tencentcloudapi.com, *.ai.ap-shanghai-fsi.tencentcloudapi.com.cn, *.ai.ap-shanghai.tencentcloudapi.cn, *.ai.ap-shanghai.tencentcloudapi.com, *.ai.ap-shanghai.tencentcloudapi.com.cn, *.ai.ap-shenzhen-fsi.tencentcloudapi.cn, *.ai.ap-shenzhen-fsi.tencentcloudapi.com, *.ai.ap-shenzhen-fsi.tencentcloudapi.com.cn, *.ai.ap-shenzhen.tencentcloudapi.cn, *.ai.ap-shenzhen.tencentcloudapi.com, *.ai.ap-shenzhen.tencentcloudapi.com.cn, *",
        "FirstFailedAt": 1785160435,
        "LastFailedTime": 1785160435,
        "Operation": "create",
        "RetryCount": 0,
        "RequestId": "320e4e84-cbe0-4674-b0a3-3ad1b5fce201"
    }
}
```

