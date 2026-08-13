**Example 1: 列出所有镜像**



Input: 

```
tccli dlc ListImages --cli-unfold-argument  \
    --Keyword tcray \
    --Type Ray \
    --Page 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "CreateTime": 1772610344431,
                "Description": "Ray 集群镜像，用于 Head 和 Worker 节点",
                "Id": 4,
                "Name": "tcray-3.0.0.dev0-py311-cpu",
                "Type": "Ray",
                "UpdateTime": 1773052310425,
                "Url": "ccr.ccs.tencentyun.com/emr-image/tcray:3.0.0.dev0-py311-cpu"
            }
        ],
        "Page": 1,
        "PageSize": 10,
        "Total": 1,
        "TotalPages": 1,
        "RequestId": "f4103770-7d4a-4528-a300-e990f598018e"
    }
}
```

