**Example 1: 通用查询调用链列表**

根据 Trace ID 列表批量查询 Span，Filters 查询参数中将 Type 设置为 in ，将 Trace ID 列表通过,隔开

Input: 

```
tccli apm DescribeGeneralSpanList --cli-unfold-argument  \
    --OrderBy.Value startTime \
    --OrderBy.Key desc \
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
        "RequestId": "test-test-test",
        "Spans": [
            {
                "TraceID": "663727c6d5d4436dd1fcaa509d0f4dc0,6c2c8ebff420a8e5b2276ec799446f98,68d3062a4c559ba212a36f61c97ba8ac",
                "Logs": [
                    {
                        "Timestamp": 0,
                        "Fields": [
                            {
                                "Type": "service.name",
                                "Value": "=",
                                "Key": "java-order-service"
                            }
                        ]
                    }
                ],
                "Tags": [
                    {
                        "Type": "service.name",
                        "Value": "=",
                        "Key": "java-order-service"
                    }
                ],
                "Process": {
                    "ServiceName": "java-order-service",
                    "Tags": [
                        {
                            "Type": "service.name",
                            "Value": "=",
                            "Key": "java-order-service"
                        }
                    ]
                },
                "Timestamp": 0,
                "OperationName": "/test",
                "References": [
                    {
                        "RefType": "1",
                        "SpanID": "4q6549c49aaa",
                        "TraceID": "663727c6d5d4436dd1fcaa509d0f4dc0,6c2c8ebff420a8e5b2276ec799446f98,68d3062a4c559ba212a36f61c97ba8ac"
                    }
                ],
                "StartTime": 0,
                "Duration": 0,
                "SpanID": "1q23w1q32165",
                "StartTimeMillis": 0
            }
        ]
    }
}
```

**Example 2: 通用查询调用链列表2**

指定 Tag 过滤条件拿到 Span 列表

Input: 

```
tccli apm DescribeGeneralSpanList --cli-unfold-argument  \
    --OrderBy.Value startTime \
    --OrderBy.Key desce \
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
        "RequestId": "test-test-test",
        "Spans": [
            {
                "TraceID": "663727c6d5d4436dd1fcaa509d0f4dc0,6c2c8ebff420a8e5b2276ec799446f98,68d3062a4c559ba212a36f61c97ba8ac",
                "Logs": [
                    {
                        "Timestamp": 0,
                        "Fields": [
                            {
                                "Type": "job",
                                "Value": "=",
                                "Key": "test1"
                            }
                        ]
                    }
                ],
                "Tags": [
                    {
                        "Type": "=",
                        "Value": "java-order-service",
                        "Key": "service.name"
                    }
                ],
                "Process": {
                    "ServiceName": "java-order-service",
                    "Tags": [
                        {
                            "Type": "job",
                            "Value": "=",
                            "Key": "test2"
                        }
                    ]
                },
                "Timestamp": 0,
                "OperationName": "/testOperation",
                "References": [
                    {
                        "RefType": "1",
                        "SpanID": "qertuytw",
                        "TraceID": "663727c6d5d4436dd1fcaa509d0f4dc0,6c2c8ebff420a8e5b2276ec799446f98,68d3062a4c559ba212a36f61c97ba8ac"
                    }
                ],
                "StartTime": 0,
                "Duration": 0,
                "SpanID": "xasfvava",
                "StartTimeMillis": 0
            }
        ]
    }
}
```

