**Example 1: 示例**

产品试用状态查询接口

Input: 

```
tccli cwp DescribeProductStatus --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ReturnCode": 1,
        "ReturnMsg": "xx",
        "Data": {
            "FWUserStatus": 1,
            "CanApplyTrial": true,
            "CanNotApplyReason": "xx",
            "LastTrialTime": "xx"
        },
        "RequestId": "xx"
    }
}
```

