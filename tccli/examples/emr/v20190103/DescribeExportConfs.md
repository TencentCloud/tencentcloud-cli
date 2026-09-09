**Example 1: 查询导出配置**



Input: 

```
tccli emr DescribeExportConfs --cli-unfold-argument  \
    --InstanceId emr-cf5zdrxk \
    --ExportConfContexts.0.ServiceType 1 \
    --ExportConfContexts.0.FileName hdfs-site.xml
```

Output: 
```
{
    "Response": {
        "ExportConfParamList": [
            {
                "Classification": "hdfs-site.xml",
                "Properties": "e30=",
                "ServiceName": "HDFS",
                "ServiceVersion": "2.7.3"
            }
        ],
        "RequestId": "6215c325-6cb9-4db4-b4bd-0c71a4f7c43d"
    }
}
```

