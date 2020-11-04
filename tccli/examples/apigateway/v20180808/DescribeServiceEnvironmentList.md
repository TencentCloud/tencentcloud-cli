**Example 1: DescribeServiceEnvironmentList**



Input: 

```
tccli apigateway DescribeServiceEnvironmentList --cli-unfold-argument  \
    --ServiceId service-ody35h5e
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 3,
            "EnvironmentList": [
                {
                    "EnvironmentName": "test",
                    "Url": "service-ody35h5e-1251006373.cq.apigw.tencentcs.com/test",
                    "Status": 1,
                    "VersionName": "202002161926124aa59df4-7198-4f7a-acc7-887ab7ee0215"
                },
                {
                    "EnvironmentName": "prepub",
                    "Url": "service-ody35h5e-1251006373.cq.apigw.tencentcs.com/prepub",
                    "Status": 0,
                    "VersionName": ""
                },
                {
                    "EnvironmentName": "release",
                    "Url": "service-ody35h5e-1251006373.cq.apigw.tencentcs.com/release",
                    "Status": 0,
                    "VersionName": ""
                }
            ]
        },
        "RequestId": "86bacb87-47ca-4295-b1e1-280956f2803b"
    }
}
```

