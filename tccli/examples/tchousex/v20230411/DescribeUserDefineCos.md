**Example 1: TEST**

查询用户是否有使用自定义COS的权限

Input: 

```
tccli tchousex DescribeUserDefineCos --cli-unfold-argument  \
    --ApiType CheckCosBucketValid \
    --CheckTypes cos_empty \
    --InstanceVersion 1.6.0_REL \
    --CosBucket jy-test-cos2-1301087413
```

Output: 
```
{
    "Response": {
        "RequestId": "",
        "ApiType": "CheckCosBucketValid",
        "ReturnData": "{\"Valid\":true,\"NotValidType\":\"\",\"NotValidMsg\":\"\"}",
        "ErrorMsg": ""
    }
}
```

