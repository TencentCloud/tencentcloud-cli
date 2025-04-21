**Example 1: 上网拦截报表(上网拦截概览)**

上网拦截报表(上网拦截概览)

Input: 

```
tccli ioa DescribeLogTimeHistogram --cli-unfold-argument  \
    --LogId EndpointAccessControl \
    --Interval day \
    --HistogramField @timestamp \
    --Field Client.Name \
    --StartTime 1682870400000 \
    --EndTime 1684857599000
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Count": 2,
                "Time": "2023-05-15T00:00:00Z",
                "Timestamp": 1684108800000,
                "TotalCount": 3
            },
            {
                "Count": 1,
                "Time": "2023-05-16T00:00:00Z",
                "Timestamp": 1684195200000,
                "TotalCount": 4
            },
            {
                "Count": 1,
                "Time": "2023-05-17T00:00:00Z",
                "Timestamp": 1684281600000,
                "TotalCount": 5
            }
        ],
        "RequestId": "9b3a9216-3ba8-4c0d-8566-97e9f75a89c7"
    }
}
```

**Example 2: 风险分析报表(产生风险事件的用户趋势)**

风险分析报表(产生风险事件的用户趋势)

Input: 

```
tccli ioa DescribeLogTimeHistogram --cli-unfold-argument  \
    --LogId UEBA \
    --Interval day \
    --HistogramField @timestamp \
    --Field Body.account_id \
    --StartTime 1682870400000 \
    --EndTime 1684857599000
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Count": 1,
                "Time": "2023-05-19T00:00:00Z",
                "Timestamp": 1684454400000,
                "TotalCount": 2
            },
            {
                "Count": 0,
                "Time": "2023-05-20T00:00:00Z",
                "Timestamp": 1684540800000,
                "TotalCount": 0
            },
            {
                "Count": 0,
                "Time": "2023-05-21T00:00:00Z",
                "Timestamp": 1684627200000,
                "TotalCount": 0
            },
            {
                "Count": 1,
                "Time": "2023-05-22T00:00:00Z",
                "Timestamp": 1684713600000,
                "TotalCount": 1
            },
            {
                "Count": 1,
                "Time": "2023-05-23T00:00:00Z",
                "Timestamp": 1684800000000,
                "TotalCount": 4
            }
        ],
        "RequestId": "b3e928b5-e3d4-4ce6-b508-39a43fe2ed52"
    }
}
```

