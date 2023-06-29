**Example 1: DescribeEdgeUnitApplicationVisualization**



Input: 

```
tccli iecp DescribeEdgeUnitApplicationVisualization --cli-unfold-argument  \
    --ApplicationId 1 \
    --EdgeUnitId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "5ebf13a2-f925-4ba7-adff-ddbc21d355e3",
        "BasicInfo": null,
        "BasicConfig": null,
        "Volumes": [],
        "InitContainers": [],
        "Containers": [],
        "Service": null,
        "Job": null,
        "CronJob": null,
        "RestartPolicy": null,
        "HorizontalPodAutoscaler": null,
        "ImagePullSecrets": []
    }
}
```

