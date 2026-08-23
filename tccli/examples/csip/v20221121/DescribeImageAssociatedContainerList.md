**Example 1: 查询镜像关联容器资产**



Input: 

```
tccli csip DescribeImageAssociatedContainerList --cli-unfold-argument  \
    --MemberId mem-12e1se11 \
    --Id 806
```

Output: 
```
{
    "Response": {
        "ContainerList": [
            {
                "ClusterId": "cls-********",
                "ClusterName": "yan***",
                "ClusterStatus": "Running",
                "ContainerId": "cc51f61a9ae01****************3f276c89cfefd****************0f125b",
                "ContainerName": "open****-**",
                "OwnerAccountName": "70000*******",
                "OwnerAppId": 260000000,
                "OwnerUin": "70000*******"
            }
        ],
        "TotalCount": 4,
        "RequestId": "9313572c-b43a-4462-aa9c-542b452c7e62"
    }
}
```

