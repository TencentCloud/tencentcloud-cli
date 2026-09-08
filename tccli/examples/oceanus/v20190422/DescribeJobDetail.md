**Example 1: demo**



Input: 

```
tccli oceanus DescribeJobDetail --cli-unfold-argument  \
    --JobSerialId cql-2xvd \
    --Path /overview
```

Output: 
```
{
    "Response": {
        "RequestId": "099s-xset-xasd-x2sd",
        "Data": "{\"taskmanagers\":1,\"slots-total\":1,\"slots-available\":0,\"jobs-running\":1,\"jobs-finished\":0,\"jobs-cancelled\":0,\"jobs-failed\":0,\"flink-version\":\"1.13.6\",\"flink-commit\":\"9cfdad4\"}"
    }
}
```

