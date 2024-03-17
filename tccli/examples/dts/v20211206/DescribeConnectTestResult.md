**Example 1: 查询连通性任务检查结果**



Input: 

```
tccli dts DescribeConnectTestResult --cli-unfold-argument  \
    --TaskIds 25014
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "IsPass": 0,
                "SNatIp": "11.163.0.0/16",
                "Status": "finished",
                "TaskId": 25014,
                "TestItems": [
                    {
                        "Code": 0,
                        "Message": "ok",
                        "TestName": "Telnet"
                    },
                    {
                        "Code": -1,
                        "Message": "无法连接源实例。请排查以下配置:1.确认账号密码是否正确; 2.请确认root能在所有IP访问数据库; error: 连通性测试错误：Error 1045: Access denied for user 'root'@'169.254.128.1' (using password: YES)。; \n详细排查手册请参考：https://cloud.tencent.com/document/product/571/62989;",
                        "TestName": "Database Connect"
                    }
                ]
            }
        ],
        "RequestId": "0cefa300-ba9c-11ee-b2d8-cfb8d1efb0e5",
        "TotalCount": 1
    }
}
```

