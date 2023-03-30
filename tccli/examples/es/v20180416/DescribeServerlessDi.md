**Example 1: 查询serverless数据接入**

查询serverless数据接入

Input: 

```
tccli es DescribeServerlessDi --cli-unfold-argument  \
    --ServerlessId index-xxx \
    --DiIds id-xx \
    --Offset 0 \
    --Limit 0 \
    --OrderBy desc \
    --Order 1
```

Output: 
```
{
    "Response": {
        "DiDataList": [
            {
                "DiId": "id-xx",
                "CreateTime": "xx-xx",
                "Status": 0,
                "DiDataSourceCvm": {
                    "VpcId": "vpc-xx",
                    "CollectorId": "co-xx",
                    "LogPaths": [
                        "/data"
                    ],
                    "CvmInstances": [
                        {
                            "InstanceId": "ins-xx",
                            "VpcId": "vpc-xx",
                            "SubnetId": "subnet-xx",
                            "ErrMsg": "err-xx"
                        }
                    ]
                },
                "DiDataSourceTke": {
                    "VpcId": "vpc-xx",
                    "CollectorId": "co-xx"
                },
                "DiDataSinkServerless": {
                    "ServerlessId": "index-xx"
                }
            }
        ],
        "TotalCount": 0,
        "RequestId": "xx-xx"
    }
}
```

