**Example 1: 查询标签值**



Input: 

```
tccli pts DescribeLabelValues --cli-unfold-argument  \
    --JobId 123 \
    --ScenarioId 123 \
    --ProjectId project-xx \
    --Metric pts_engine_req_total \
    --LabelName service
```

Output: 
```
{
    "Response": {
        "LabelValueSet": [
            "http://pets.com/0",
            "http://pets.com/1",
            "http://pets.com/10",
            "http://pets.com/11",
            "http://pets.com/12",
            "http://pets.com/13",
            "http://pets.com/14",
            "http://pets.com/15",
            "http://pets.com/16",
            "http://pets.com/17",
            "http://pets.com/18",
            "http://pets.com/19",
            "http://pets.com/2",
            "http://pets.com/3",
            "http://pets.com/4",
            "http://pets.com/5",
            "http://pets.com/6",
            "http://pets.com/7",
            "http://pets.com/8",
            "http://pets.com/9"
        ],
        "RequestId": "xx"
    }
}
```

