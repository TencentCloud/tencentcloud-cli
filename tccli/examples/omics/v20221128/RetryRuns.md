**Example 1: 重试任务批次**

重试任务批次。

Input: 

```
tccli omics RetryRuns --cli-unfold-argument  \
    --ProjectId prj-aggressive-lime-porcupine-752427 \
    --RunGroupId run-ashamed-bleak-doggy-247963
```

Output: 
```
{
    "Response": {
        "RequestId": "46520c37-4d28-49e1-a738-01f64ae1b06b",
        "RunGroupId": "run-greedy-ecru-bonobo-459181"
    }
}
```

**Example 2: 重试单个任务**

重试单个任务。

Input: 

```
tccli omics RetryRuns --cli-unfold-argument  \
    --ProjectId prj-aggressive-lime-porcupine-752427 \
    --RunUuids 7b501b32-4e42-456a-9d54-aa3c9791beb0
```

Output: 
```
{
    "Response": {
        "RequestId": "e2fe59bb-21e3-45de-9289-9d22a5b1bdff",
        "RunGroupId": "run-lonely-orange-dodo-410909"
    }
}
```

**Example 3: 重试任务批次内指定任务**

重试任务批次内指定任务。

Input: 

```
tccli omics RetryRuns --cli-unfold-argument  \
    --ProjectId prj-aggressive-lime-porcupine-752427 \
    --RunGroupId run-ashamed-bleak-doggy-247963 \
    --RunUuids 7b501b32-4e42-456a-9d54-aa3c9791beb0 38b860fa-65d3-4adc-8000-4c0c31d2ff51
```

Output: 
```
{
    "Response": {
        "RequestId": "e5dc747d-7ad2-44de-afe5-569c9a342db8",
        "RunGroupId": "run-pretty-yellow-mastiff-141933"
    }
}
```

