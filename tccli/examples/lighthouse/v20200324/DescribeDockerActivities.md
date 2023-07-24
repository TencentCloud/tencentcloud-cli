**Example 1: 查询Docker容器列表**



Input: 

```
tccli lighthouse DescribeDockerActivities --cli-unfold-argument  \
    --ActivityIds lhda-nn82v77w \
    --InstanceId lhins-nwycpjl3
```

Output: 
```
{
    "Response": {
        "DockerActivitySet": [
            {
                "ActivityCommandOutput": "ODM4YjA3ODE5MjVmOGVhOThmZjE4MzFjNjBmMWU2MTc4YzIxOTIzMTkyZWM3NzNjYjBjYjg0MjdmZTE5NmZhMwo=",
                "ActivityId": "lhda-8jkefl3i",
                "ActivityName": "RestartDockerContainers",
                "ActivityState": "SUCCESS",
                "ContainerIds": [
                    "838b0781925f8ea98ff1831c60f1e6178c21923192ec773cb0cb8427fe196fa3"
                ],
                "CreatedTime": "2021-07-13T08:08:00Z",
                "EndTime": "2021-07-13T08:08:06Z"
            }
        ],
        "RequestId": "6d88ebe5-9267-41af-9797-cb02603b6909",
        "TotalCount": 1
    }
}
```

