**Example 1: DescribeServiceEnvironmentStrategy**



Input: 

```
tccli apigateway DescribeServiceEnvironmentStrategy --cli-unfold-argument  \
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
                    "EnvironmentName": "prepub",
                    "Url": "service-ody35h5e-1251006373.cq.apigw.tencentcs.com/prepub",
                    "Status": 0,
                    "Strategy": 5000,
                    "VersionName": ""
                },
                {
                    "EnvironmentName": "test",
                    "Url": "service-ody35h5e-1251006373.cq.apigw.tencentcs.com/test",
                    "Status": 1,
                    "Strategy": 30,
                    "VersionName": "202002161926124aa59df4-7198-4f7a-acc7-887ab7ee0215"
                },
                {
                    "EnvironmentName": "release",
                    "Url": "service-ody35h5e-1251006373.cq.apigw.tencentcs.com/release",
                    "Status": 0,
                    "VersionName": "",
                    "Strategy": 5000
                }
            ]
        },
        "RequestId": "0d660a03-92b1-4062-aa04-aee837818ba5"
    }
}
```

