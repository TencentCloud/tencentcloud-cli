**Example 1: 查看一个策略的详情**

查看一个策略的详情

Input: 

```
tccli organization DescribePolicy --cli-unfold-argument  \
    --PolicyId 1001
```

Output: 
```
{
    "Response": {
        "RequestId": "152482ca-5968-4557-ac1d-1e7ac28ce0da",
        "AddTime": "2022-08-04 16:04:17",
        "Description": "test",
        "PolicyDocument": "{\"strategyInfo\":{\"version\":\"2.0\",\"statement\":[{\"effect\":\"allow\",\"action\":\"*\",\"resource\":\"qcs::cam::*:*\"}]},\"version\":\"2.0\"}",
        "PolicyId": 1001,
        "PolicyName": "test-1",
        "Type": 3,
        "UpdateTime": "2022-08-04 17:04:17"
    }
}
```

