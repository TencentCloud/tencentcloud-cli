**Example 1: 描述服务配置**



Input: 

```
tccli tiems DescribeServiceConfigs --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "4a3d63f8-fb12-4dd5-b444-02c0a91af0d2",
        "ServiceConfigs": [
            {
                "Id": "asjcqn7wtdgrd7t",
                "Name": "test1",
                "Runtime": "pmml",
                "ModelUri": "cos://ti-ems-example.cos.ap-beijing.myqcloud.com/models/pmml/",
                "CreateTime": "2019-11-04T17:34:58+08:00",
                "UpdateTime": "2019-11-04T17:34:58+08:00",
                "Version": "1.0",
                "Description": "字符串"
            }
        ],
        "TotalCount": 1
    }
}
```

