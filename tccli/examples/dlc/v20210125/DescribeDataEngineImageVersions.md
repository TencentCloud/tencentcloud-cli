**Example 1: 获取独享集群大版本镜像列表**

本接口用于获取独享集群大版本镜像列表

Input: 

```
tccli dlc DescribeDataEngineImageVersions --cli-unfold-argument  \
    --EngineType SQL
```

Output: 
```
{
    "Response": {
        "RequestId": "b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1",
        "Total": 1,
        "ImageParentVersions": [
            {
                "UpdateTime": "2020-01-01:00:00:00",
                "Description": "测试",
                "IsSharedEngine": 1,
                "ImageVersionId": "d3018ad4-9a7e-4f64-a3f4-f38507c69742",
                "IsPublic": 1,
                "State": 1,
                "InsertTime": "2020-01-01:00:00:00",
                "ImageVersion": "SuperSQL",
                "EngineType": "SparkSQL"
            }
        ]
    }
}
```

