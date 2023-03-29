**Example 1: 查询serverless数据接入**

查询serverless数据接入

Input: 

```
tccli es DescribeServerlessDi --cli-unfold-argument  \
    --ServerlessId xx \
    --DiIds xx \
    --Offset 0 \
    --Limit 0 \
    --OrderBy xx \
    --Order xx
```

Output: 
```
{
    "Response": {
        "DiDataList": [
            {
                "DiId": "xx",
                "CreateTime": "xx",
                "Status": 0,
                "DiDataSourceCvm": {
                    "VpcId": "xx",
                    "LogPaths": [
                        "xx"
                    ],
                    "CvmInstances": [
                        {
                            "InstanceId": "xx",
                            "VpcId": "xx",
                            "SubnetId": "xx",
                            "ErrMsg": "xx"
                        }
                    ]
                },
                "DiDataSourceTke": {
                    "VpcId": "xx"
                },
                "DiDataSinkServerless": {
                    "ServerlessId": "xx"
                }
            }
        ],
        "TotalCount": 0,
        "RequestId": "xx"
    }
}
```

