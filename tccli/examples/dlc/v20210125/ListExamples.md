**Example 1: ListExamples**

分页查询案例列表

Input: 

```
tccli dlc ListExamples --cli-unfold-argument  \
    --Category data-processing \
    --Keyword 批量 \
    --Tags ETL \
    --OrderBy Popularity \
    --Page 1 \
    --PageSize 2
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "Category": "data-processing",
                "CodeArchiveUrl": "https://common-job-packages-251233710.cos.ap-guangzhou.myqcloud.com/models/examples/example-005-raydp-raydata.zip",
                "CreateTime": 1779764566348,
                "Deleted": 0,
                "Description": "使用 RayDP (Spark on Ray) 进行分布式数据预处理，再通过 Ray Data 进行分布式批量推理，构建端到端 ML 流水线",
                "Difficulty": "advanced",
                "EstimatedTime": 25,
                "ExampleId": "example-005-raydp-raydata",
                "Id": 9,
                "Image": "ccr.ccs.tencentyun.com/emr-image/tcray:2.55.1-py311-cpu-extra",
                "IsEnabled": true,
                "LabImage": "ccr.ccs.tencentyun.com/emr-image/tcray:2.55.1-py311-cpu-extra-lab",
                "Popularity": 3,
                "ResourceConfig": "{\"Head\":{\"Name\":\"default-head\",\"PodCpu\":2,\"PodMem\":4,\"PodNum\":1},\"Worker\":[{\"Name\":\"default-worker\",\"PodCpu\":2,\"PodMem\":4,\"MinPodNum\":1,\"MaxPodNum\":1}]}",
                "SortOrder": 5,
                "Tags": [
                    "RayDP"
                ],
                "Title": "RayDP + Ray Data: Spark ETL 到分布式批量推理",
                "UpdateTime": 1779764566348
            }
        ],
        "Page": 1,
        "PageSize": 2,
        "Total": 1,
        "TotalPages": 1,
        "RequestId": "d5e4e25a-7505-42a5-85dc-a8d9b2f30e40"
    }
}
```

