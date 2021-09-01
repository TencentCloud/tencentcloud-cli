**Example 1: 指定实例ID删除serverlessDB实例**

以指定实例ID方式删除实例，删除一个实例ID为“postgres-xxxxx”的serverless实例。

Input: 

```
tccli postgres DeleteServerlessDBInstance --cli-unfold-argument  \
    --DBInstanceId postgres-xxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "08fdf411-5d39-44f2-8e1d-a58ee60b237d"
    }
}
```

**Example 2: 指定实例名删除serverlessDB实例**

以指定实例名方式删除实例，删除一个实例名为“serverlessdb-test”的serverless实例。

Input: 

```
tccli postgres DeleteServerlessDBInstance --cli-unfold-argument  \
    --DBInstanceName serverlessdb-test
```

Output: 
```
{
    "Response": {
        "RequestId": "08fdf411-5d39-44f2-8e1d-a58ee60b237d"
    }
}
```

