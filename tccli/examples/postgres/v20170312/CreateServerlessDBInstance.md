**Example 1: 创建serverlessDB实例**

创建一个实例名为“serverlessdb-test”的serverless实例，实例数据库版本为10.4，服务端database字符集为UTF8。

Input: 

```
tccli postgres CreateServerlessDBInstance --cli-unfold-argument  \
    --Zone ap-guangzhou-3 \
    --VpcId vpc-xxxx \
    --SubnetId subnet-xxx \
    --DBInstanceName serverlessdb-test \
    --DBVersion 10.4 \
    --DBCharset UTF8
```

Output: 
```
{
    "Response": {
        "RequestId": "08fdf411-5d39-44f2-8e1d-a58ee60b237d",
        "DBInstanceId": "postgres-xxxxx"
    }
}
```

