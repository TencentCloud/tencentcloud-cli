**Example 1: 请求示例**

查询指定实例的账号信息

Input: 

```
tccli redis DescribeInstanceAccount --cli-unfold-argument  \
    --InstanceId crs-5a4py64p \
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
                "InstanceId": "crs-mufy7q15",
                "Privilege": "rw",
                "ReadonlyPolicy": [
                    "master",
                    "replication"
                ],
                "Remark": "default",
                "Status": 2
            }
        ],
        "RequestId": "b97a9706-dee2-4d5c-8f2d-84873bc79629",
        "TotalCount": 1
    }
}
```

