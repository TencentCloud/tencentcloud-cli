**Example 1: DescribeContainerEvents**



Input: 

```
tccli tsf DescribeContainerEvents --cli-unfold-argument  \
    --ResourceType instance \
    --ResourceId test-event-6f46bcb6b-sxfcr \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "RequestId": "4bf8bc01-2786-4341-be2b-c6610556026e",
        "Result": {
            "TotalCount": 1,
            "Content": [
                {
                    "FirstTimestamp": "2021-02-07T18:32:12Z",
                    "LastTimestamp": "2021-02-07T18:32:12Z",
                    "Type": "Normal/Warning",
                    "Kind": "Pod",
                    "Name": "shop-demo-7ff965d54d-65rlw.1668ccf6e4263fde",
                    "Reason": "Pulled",
                    "Message": "0/1 nodes are available: 1 Insufficient memory.",
                    "Count": 3
                }
            ]
        }
    }
}
```

