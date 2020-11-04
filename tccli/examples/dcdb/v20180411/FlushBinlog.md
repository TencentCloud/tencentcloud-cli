**Example 1: 切分Binlog**

当需要最新的binlog文件时调用。
该api相当于在mysqld中执行flush logs。binlog切分后将自动上传到cos，展示在控制台分片的binlog列表里，用户可下载。

Input: 

```
tccli dcdb FlushBinlog --cli-unfold-argument  \
    --InstanceId tdsql-avw0207d
```

Output: 
```
{
    "Response": {
        "RequestId": "8ce27ff0-7fe1-11ea-8469-525400542aa6"
    }
}
```

