**Example 1: 去重查询调用链列表**

根据traceId列表批量查询去重span，Filters查询参数中将Type设置为in，将traceId列表通过,隔开。

Input: 

```
tccli apm DescribeApmPAASDeduplicateSpanList --cli-unfold-argument  \
    --OrderBy.Key abc \
    --OrderBy.Value abc \
    --StartTime 0 \
    --EndTime 0 \
    --InstanceId abc \
    --Filters.0.Type abc \
    --Filters.0.Key abc \
    --Filters.0.Value abc \
    --BusinessName abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Spans": [
            {
                "TraceID": "abc",
                "Logs": [
                    {
                        "Timestamp": 0,
                        "Fields": [
                            {
                                "Type": "abc",
                                "Key": "abc",
                                "Value": "abc"
                            }
                        ]
                    }
                ],
                "Tags": [
                    {
                        "Type": "abc",
                        "Key": "abc",
                        "Value": "abc"
                    }
                ],
                "Process": {
                    "ServiceName": "abc",
                    "Tags": [
                        {
                            "Type": "abc",
                            "Key": "abc",
                            "Value": "abc"
                        }
                    ]
                },
                "Timestamp": 0,
                "OperationName": "abc",
                "References": [
                    {
                        "RefType": "abc",
                        "SpanID": "abc",
                        "TraceID": "abc"
                    }
                ],
                "StartTime": 0,
                "Duration": 0,
                "SpanID": "abc",
                "StartTimeMillis": 0,
                "ParentSpanID": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

