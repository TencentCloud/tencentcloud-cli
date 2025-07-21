**Example 1: 查询指定站点在指定计费大区的内容加速流量**

查询指定 zone-id 在指定 region-id 下的内容加速流量计费用量，查询时间粒度为天。

Input: 

```
tccli teo DescribeBillingData --cli-unfold-argument  \
    --StartTime 2024-01-01T00:00:00+08:00 \
    --EndTime 2024-01-24T03:20:00+08:00 \
    --Interval day \
    --MetricName acc_flux \
    --Filters.0.Type region-id \
    --Filters.0.Value MidEast \
    --ZoneIds zone-2smdfso9dr58
```

Output: 
```
{
    "Response": {
        "RequestId": "457e8933-4296-4878-9a7f-fb888559e29e",
        "Data": [
            {
                "Time": "2023-12-31T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-01T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-02T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-03T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-04T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-05T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-06T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-07T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-08T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-09T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-10T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-11T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-12T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-13T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-14T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-15T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-16T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-17T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-18T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-19T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-20T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-21T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-22T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-23T16:00:00Z",
                "Value": 0
            }
        ]
    }
}
```

**Example 2: 查询指定站点的内容加速流量，并按照站点 ID 分组**

查询指定 zone-id 的内容加速流量计费用量，并按照 zone-id 进行分组，查询时间粒度为天。

Input: 

```
tccli teo DescribeBillingData --cli-unfold-argument  \
    --StartTime 2025-07-01T00:00:00+08:00 \
    --EndTime 2025-07-02T23:59:59+08:00 \
    --Interval day \
    --MetricName acc_flux \
    --ZoneIds zone-2m2gq4dnpmd2 zone-30hqppzribht \
    --GroupBy zone-id
```

Output: 
```
{
    "Response": {
        "RequestId": "d2174285-8aac-4cdc-bc06-d81f2f6520da",
        "Data": [
            {
                "Time": "2025-06-30T16:00:00Z",
                "Value": 0,
                "ZoneId": "zone-2m2gq4dnpmd2"
            },
            {
                "Time": "2025-07-01T16:00:00Z",
                "Value": 2751240612,
                "ZoneId": "zone-2m2gq4dnpmd2"
            },
            {
                "Time": "2025-06-30T16:00:00Z",
                "Value": 0,
                "ZoneId": "zone-30hqppzribht"
            },
            {
                "Time": "2025-07-01T16:00:00Z",
                "Value": 68443435,
                "ZoneId": "zone-30hqppzribht"
            }
        ]
    }
}
```

**Example 3: 查询指定站点的内容加速流量，并按照域名分组**

查询指定 zone-id 的内容加速流量计费用量，并按照域名进行分组，查询时间粒度为天。

Input: 

```
tccli teo DescribeBillingData --cli-unfold-argument  \
    --StartTime 2025-07-01T00:00:00+08:00 \
    --EndTime 2025-07-02T23:59:59+08:00 \
    --Interval day \
    --MetricName acc_flux \
    --ZoneIds zone-2m2gq4dnpmd2 zone-30hqppzribht \
    --GroupBy host
```

Output: 
```
{
    "Response": {
        "RequestId": "d2174285-8aac-4cdc-bc06-d81f2f6520da",
        "Data": [
            {
                "Host": "test1.example.com",
                "Time": "2025-06-30T16:00:00Z",
                "Value": 1387001003,
                "ZoneId": "zone-2m2gq4dnpmd2"
            },
            {
                "Host": "test1.example.com",
                "Time": "2025-07-01T16:00:00Z",
                "Value": 1390529805,
                "ZoneId": "zone-2m2gq4dnpmd2"
            },
            {
                "Host": "test2.example.com",
                "Time": "2025-06-30T16:00:00Z",
                "Value": 2879078,
                "ZoneId": "zone-2m2gq4dnpmd2"
            },
            {
                "Host": "test2.example.com",
                "Time": "2025-07-01T16:00:00Z",
                "Value": 2889084,
                "ZoneId": "zone-2m2gq4dnpmd2"
            }
        ]
    }
}
```

**Example 4: 查询指定站点的内容加速流量，并按照站点 ID 和计费大区分组**

查询指定 zone-id 的内容加速流量计费用量，并按照 zone-id 和计费大区进行分组，查询时间粒度为天。

Input: 

```
tccli teo DescribeBillingData --cli-unfold-argument  \
    --StartTime 2025-07-01T00:00:00+08:00 \
    --EndTime 2025-07-02T23:59:59+08:00 \
    --Interval day \
    --MetricName acc_flux \
    --ZoneIds zone-2m2gq4dnpmd2 zone-30hqppzribht \
    --GroupBy zone-id region-id
```

Output: 
```
{
    "Response": {
        "RequestId": "d2174285-8aac-4cdc-bc06-d81f2f6520da",
        "Data": [
            {
                "RegionId": "SA",
                "Time": "2025-06-30T16:00:00Z",
                "Value": 549591531,
                "ZoneId": "zone-2m2gq4dnpmd2"
            },
            {
                "RegionId": "SA",
                "Time": "2025-07-01T16:00:00Z",
                "Value": 549591531,
                "ZoneId": "zone-2m2gq4dnpmd2"
            },
            {
                "RegionId": "MidEast",
                "Time": "2025-06-30T16:00:00Z",
                "Value": 549591531,
                "ZoneId": "zone-30hqppzribht"
            },
            {
                "RegionId": "MidEast",
                "Time": "2025-07-01T16:00:00Z",
                "Value": 549591531,
                "ZoneId": "zone-30hqppzribht"
            }
        ]
    }
}
```

