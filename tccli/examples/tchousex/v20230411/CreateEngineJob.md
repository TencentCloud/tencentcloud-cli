**Example 1: 测试示例**

测试示例

Input: 

```
tccli tchousex CreateEngineJob --cli-unfold-argument  \
    --InstanceId warehouse-qiwlg758 \
    --JobContent  \
    --JobUUID 123xxxxxx \
    --ExecuteUser test \
    --ExecutePassword test \
    --ResourcePath cosn://yihang-cq-spark-1301087413/spark-examples_2.12-3.2.3.jar \
    --Parameters.0.Name DriverCores \
    --Parameters.0.Value 1 \
    --Parameters.1.Name ExecutorCores \
    --Parameters.1.Value 1 \
    --Parameters.2.Name NumExecutors \
    --Parameters.2.Value 1 \
    --ExtParameters.0.Name ClassName \
    --ExtParameters.0.Value org.apache.spark.examples.SparkPi
```

Output: 
```
{
    "Response": {
        "EngineJobId": "batch-task-dmrqzc",
        "EngineJobLogUrl": "https://console.cloud.tencent.com/tchousex/sql-task?region=ap-chongqing&instanceId=warehouse-qiwlg758",
        "ErrorMsg": "",
        "RequestId": "dda09472-2d28-4598-bf0d-631861bb70d2"
    }
}
```

**Example 2: spark sql测试示例**

spark sql测试示例

Input: 

```
tccli tchousex CreateEngineJob --cli-unfold-argument  \
    --InstanceId warehouse-6oxa1th8 \
    --JobType tchousex \
    --JobContent LyorZW5naW5lPWJhdGNoKi9zZWxlY3QgMTtzZWxlY3QgMQ== \
    --JobUUID 123 \
    --ExecuteUser bobpeng \
    --ExecutePassword Abc123456 \
    --Parameters.0.Name VirtualCluster \
    --Parameters.0.Value chengjintest1
```

Output: 
```
{
    "Response": {
        "EngineJobId": "sql-task-uiw9w3",
        "EngineJobLogUrl": "https://console.cloud.tencent.com/tchousex/sql-task-detail?region=ap-guangzhou&instanceId=warehouse-6oxa1th8&taskId=sql-task-uiw9w3&tab=run-log",
        "RequestId": "1d423487-c83e-4a64-841d-ad845392ed35"
    }
}
```

**Example 3: sql工作区请求示例**

sql工作区请求示例

Input: 

```
tccli tchousex CreateEngineJob --cli-unfold-argument  \
    --InstanceId warehouse-ooj2s44q \
    --JobType tchousex \
    --JobContent c2VsZWN0ICogZnJvbSB0ZXN0LmxpbmVpdGVtIGxpbWl0IDIwMDA= \
    --JobUUID 123 \
    --ExecuteUser root \
    --ExecutePassword Abc123456 \
    --Parameters.0.Name VirtualCluster \
    --Parameters.0.Value bob-test
```

Output: 
```
{
    "Response": {
        "EngineJobId": "tchousex-3dsnag",
        "EngineJobLogUrl": "",
        "RequestId": "676b4f21-9bc4-4531-9d56-04041b699389"
    }
}
```

