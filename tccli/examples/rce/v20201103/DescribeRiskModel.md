**Example 1: DescribeRiskModel 请求与相应**



Input: 

```
tccli rce DescribeRiskModel --cli-unfold-argument  \
    --BusinessSecurityData.UserData H4sIAAAAAAAEAOy9a3Mb2XUu/Fe2xieyJibAvl8YO54mAJIgCRACwIs0nHI1gSbZItANoQFSlMun4tSxnUs5OfVWTaXiylv5YH+w/UG+5LhOPtl/ZZI/8P6Fd621uxsNsEFxNzXUKBnNjIYE+rL32nuv+3rW9z+a+EMvmriJOvcQ+8zDPBcmZVOjiRokpv6xCLONTnKBLIs0EVB2dXXTfiZxEpVVFclWqptvwjYPUoReeVtM89ZCO6LbZ/cLHWG3fvhv1P1hQPmm5Xf4ac1B2H5gdVKJRDqqgvEPe/D+6eefFvmymsK/fPPTZf7n/wXylbZ5xMgFAA== \
    --BusinessSecurityData.ApplyDate 1631429799 \
    --BusinessSecurityData.UserId 088a3a92-1fb3-4e6a-8c3d-c458619779bd
```

Output: 
```
{
    "Response": {
        "Data": {
            "Code": 0,
            "Message": "OK",
            "Value": {
                "ApplyScore": 89.11
            }
        },
        "RequestId": "a6227506-5f00-43cf-9a4c-66fe931cefc9"
    }
}
```

