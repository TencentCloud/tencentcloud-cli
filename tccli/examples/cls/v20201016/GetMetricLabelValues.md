**Example 1: 获取时序label values列表**

获取时序label values列表

Input: 

```
tccli cls GetMetricLabelValues --cli-unfold-argument  \
    --TopicId 3a05cb9c-3471-42b8-b212-6ecbc0c49a4a \
    --LabelName __name__ \
    --Start 1772787397 \
    --End 1772787697
```

Output: 
```
{
    "Response": {
        "Values": [
            "http_server_requests_seconds_count"
        ],
        "RequestId": "7ab209e6-fa54-4583-997a-86fafb9cd32a"
    }
}
```

