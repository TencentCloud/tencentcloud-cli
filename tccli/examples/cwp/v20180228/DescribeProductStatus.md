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
        "ReturnMsg": "msg",
        "Data": {
            "FWUserStatus": 1,
            "CanApplyTrial": true,
            "CanNotApplyReason": "reason",
            "LastTrialTime": " 2019-12-25 11:57:15"
        },
        "RequestId": "xxxxxxxx-1234-5678-9101-yyyyyyyyyy"
    }
}
```

