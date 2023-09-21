**Example 1: 通用查询调用链列表**

根据traceId列表批量查询span，Filters查询参数中将Type设置为in，将traceId列表通过,隔开。

Input: 

```
tccli apm DescribeGeneralSpanList --cli-unfold-argument  \
    --OrderBy.Value xx \
    --OrderBy.Key xx \
    --Filters.0.Key traceID \
    --Filters.0.Type in \
    --Filters.0.Value 663727c6d5d4436dd1fcaa509d0f4dc0,6c2c8ebff420a8e5b2276ec799446f98,68d3062a4c559ba212a36f61c97ba8ac \
    --Limit 0 \
    --Offset 10 \
    --InstanceId 52Dpv13GR \
    --BusinessName tdmq
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "RequestId": "xx",
        "Spans": [
            {
                "TraceID": "xx",
                "Logs": [
                    {
                        "Timestamp": 0,
                        "Fields": [
                            {
                                "Type": "xx",
                                "Value": "xx",
                                "Key": "xx"
                            }
                        ]
                    }
                ],
                "Tags": [
                    {
                        "Type": "xx",
                        "Value": "xx",
                        "Key": "xx"
                    }
                ],
                "Process": {
                    "ServiceName": "xx",
                    "Tags": [
                        {
                            "Type": "xx",
                            "Value": "xx",
                            "Key": "xx"
                        }
                    ]
                },
                "Timestamp": 0,
                "OperationName": "xx",
                "References": [
                    {
                        "RefType": "xx",
                        "SpanID": "xx",
                        "TraceID": "xx"
                    }
                ],
                "StartTime": 0,
                "Duration": 0,
                "SpanID": "xx",
                "StartTimeMillis": 0
            }
        ]
    }
}
```

**Example 2: 通用查询调用链列表2**

指定tag过滤条件拿到span列表。

Input: 

```
tccli apm DescribeGeneralSpanList --cli-unfold-argument  \
    --OrderBy.Value xx \
    --OrderBy.Key xx \
    --Filters.0.Key pulsar:sub_name \
    --Filters.0.Type = \
    --Filters.0.Value participants \
    --Limit 0 \
    --Offset 10 \
    --InstanceId 52Dpv13GR \
    --BusinessName tdmq \
    --StartTime 1621923035
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "RequestId": "xx",
        "Spans": [
            {
                "TraceID": "xx",
                "Logs": [
                    {
                        "Timestamp": 0,
                        "Fields": [
                            {
                                "Type": "xx",
                                "Value": "xx",
                                "Key": "xx"
                            }
                        ]
                    }
                ],
                "Tags": [
                    {
                        "Type": "xx",
                        "Value": "xx",
                        "Key": "xx"
                    }
                ],
                "Process": {
                    "ServiceName": "xx",
                    "Tags": [
                        {
                            "Type": "xx",
                            "Value": "xx",
                            "Key": "xx"
                        }
                    ]
                },
                "Timestamp": 0,
                "OperationName": "xx",
                "References": [
                    {
                        "RefType": "xx",
                        "SpanID": "xx",
                        "TraceID": "xx"
                    }
                ],
                "StartTime": 0,
                "Duration": 0,
                "SpanID": "xx",
                "StartTimeMillis": 0
            }
        ]
    }
}
```

