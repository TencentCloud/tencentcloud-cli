**Example 1: 设置Fleet扩缩容的容量配置**



Input: 

```
tccli gse UpdateFleetCapacity --cli-unfold-argument  \
    --FleetId fleet-qp3g3caa-ay03mhdm \
    --DesiredInstances 30 \
    --MinSize 0 \
    --MaxSize 40
```

Output: 
```
{
    "Response": {
        "FleetId": "fleet-qp3g3caa-19tzbzao",
        "RequestId": "ada0f201-91c7-4100-bbb4-a29e7399e776"
    }
}
```

