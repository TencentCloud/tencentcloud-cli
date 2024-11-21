**Example 1: 请求示例**

查询指定实例的账号信息

Input: 

```
tccli redis DescribeInstanceAccount --cli-unfold-argument  \
    --InstanceId crs-fswdmXXX \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Accounts": [
            {
                "AccountName": "root",
                "CreateTime": "",
                "InstanceId": "crs-fswdmXXX",
                "Privilege": "rw",
                "ReadonlyPolicy": [
                    "master"
                ],
                "Remark": "default",
                "Status": 2
            }
        ],
        "RequestId": "10369b9b-b514-48b1-8967-44448fe8XXXXX",
        "TotalCount": 1
    }
}
```

