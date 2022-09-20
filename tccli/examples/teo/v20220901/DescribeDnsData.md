**Example 1: 获取指定站点的DNS请求数统计曲线**



Input: 

```
tccli teo DescribeDnsData --cli-unfold-argument  \
    --StartTime 2020-09-01T00:00:00+00:00 \
    --EndTime 2020-09-01T00:09:59+00:00 \
    --Filters.0.Name zone \
    --Filters.0.Values tencent.com
```

Output: 
```
{
    "Response": {
        "RequestId": "9cc50b24-7dc5-44f4-96ce-95825d53ff2f",
        "Data": [
            {
                "Time": "2020-09-01T00:00:00+00:00",
                "Value": 101
            },
            {
                "Time": "2020-09-01T00:01:00+00:00",
                "Value": 102
            },
            {
                "Time": "2020-09-01T00:02:00+00:00",
                "Value": 103
            },
            {
                "Time": "2020-09-01T00:03:00+00:00",
                "Value": 104
            },
            {
                "Time": "2020-09-01T00:04:00+00:00",
                "Value": 105
            },
            {
                "Time": "2020-09-01T00:05:00+00:00",
                "Value": 0
            },
            {
                "Time": "2020-09-01T00:06:00+00:00",
                "Value": 0
            },
            {
                "Time": "2020-09-01T00:07:00+00:00",
                "Value": 107
            },
            {
                "Time": "2020-09-01T00:08:00+00:00",
                "Value": 108
            },
            {
                "Time": "2020-09-01T00:09:00+00:00",
                "Value": 109
            }
        ]
    }
}
```

**Example 2: 获取指定站点指定域名的DNS请求数统计曲线**



Input: 

```
tccli teo DescribeDnsData --cli-unfold-argument  \
    --StartTime 2020-09-01T00:00:00+00:00 \
    --EndTime 2020-09-01T00:09:59+00:00 \
    --Filters.0.Name zone \
    --Filters.0.Values tencent.com \
    --Filters.1.Name host \
    --Filters.1.Values test.tencent.com
```

Output: 
```
{
    "Response": {
        "RequestId": "9cc50b24-7dc5-44f4-96ce-95825d53ff2f",
        "Data": [
            {
                "Time": "2020-09-01T00:00:00+00:00",
                "Value": 101
            },
            {
                "Time": "2020-09-01T00:01:00+00:00",
                "Value": 102
            },
            {
                "Time": "2020-09-01T00:02:00+00:00",
                "Value": 103
            },
            {
                "Time": "2020-09-01T00:03:00+00:00",
                "Value": 104
            },
            {
                "Time": "2020-09-01T00:04:00+00:00",
                "Value": 105
            },
            {
                "Time": "2020-09-01T00:05:00+00:00",
                "Value": 0
            },
            {
                "Time": "2020-09-01T00:06:00+00:00",
                "Value": 0
            },
            {
                "Time": "2020-09-01T00:07:00+00:00",
                "Value": 107
            },
            {
                "Time": "2020-09-01T00:08:00+00:00",
                "Value": 108
            },
            {
                "Time": "2020-09-01T00:09:00+00:00",
                "Value": 109
            }
        ]
    }
}
```

**Example 3: 获取指定站点来自亚洲和非洲的DNS请求数统计曲线**



Input: 

```
tccli teo DescribeDnsData --cli-unfold-argument  \
    --StartTime 2020-09-01T00:00:00+00:00 \
    --EndTime 2020-09-01T00:09:59+00:00 \
    --Filters.0.Name zone \
    --Filters.0.Values tencent.com \
    --Filters.1.Name area \
    --Filters.1.Values Asia Africa
```

Output: 
```
{
    "Response": {
        "RequestId": "9cc50b24-7dc5-44f4-96ce-95825d53ff2f",
        "Data": [
            {
                "Time": "2020-09-01T00:00:00+00:00",
                "Value": 101
            },
            {
                "Time": "2020-09-01T00:01:00+00:00",
                "Value": 102
            },
            {
                "Time": "2020-09-01T00:02:00+00:00",
                "Value": 103
            },
            {
                "Time": "2020-09-01T00:03:00+00:00",
                "Value": 104
            },
            {
                "Time": "2020-09-01T00:04:00+00:00",
                "Value": 105
            },
            {
                "Time": "2020-09-01T00:05:00+00:00",
                "Value": 0
            },
            {
                "Time": "2020-09-01T00:06:00+00:00",
                "Value": 0
            },
            {
                "Time": "2020-09-01T00:07:00+00:00",
                "Value": 107
            },
            {
                "Time": "2020-09-01T00:08:00+00:00",
                "Value": 108
            },
            {
                "Time": "2020-09-01T00:09:00+00:00",
                "Value": 109
            }
        ]
    }
}
```

**Example 4: 获取指定站点解析失败的DNS请求数统计曲线**



Input: 

```
tccli teo DescribeDnsData --cli-unfold-argument  \
    --StartTime 2020-09-01T00:00:00+00:00 \
    --EndTime 2020-09-01T00:09:59+00:00 \
    --Filters.0.Name zone \
    --Filters.0.Values tencent.com \
    --Filters.1.Name code \
    --Filters.1.Values NXDomain NotImp Refused
```

Output: 
```
{
    "Response": {
        "RequestId": "9cc50b24-7dc5-44f4-96ce-95825d53ff2f",
        "Data": [
            {
                "Time": "2020-09-01T00:00:00+00:00",
                "Value": 101
            },
            {
                "Time": "2020-09-01T00:01:00+00:00",
                "Value": 102
            },
            {
                "Time": "2020-09-01T00:02:00+00:00",
                "Value": 103
            },
            {
                "Time": "2020-09-01T00:03:00+00:00",
                "Value": 104
            },
            {
                "Time": "2020-09-01T00:04:00+00:00",
                "Value": 105
            },
            {
                "Time": "2020-09-01T00:05:00+00:00",
                "Value": 0
            },
            {
                "Time": "2020-09-01T00:06:00+00:00",
                "Value": 0
            },
            {
                "Time": "2020-09-01T00:07:00+00:00",
                "Value": 107
            },
            {
                "Time": "2020-09-01T00:08:00+00:00",
                "Value": 108
            },
            {
                "Time": "2020-09-01T00:09:00+00:00",
                "Value": 109
            }
        ]
    }
}
```

**Example 5: 获取指定站点所有解析A记录的DNS请求数统计曲线**



Input: 

```
tccli teo DescribeDnsData --cli-unfold-argument  \
    --StartTime 2020-09-01T00:00:00+00:00 \
    --EndTime 2020-09-01T00:09:59+00:00 \
    --Filters.0.Name zone \
    --Filters.0.Values tencent.com \
    --Filters.1.Name type \
    --Filters.1.Values A
```

Output: 
```
{
    "Response": {
        "RequestId": "9cc50b24-7dc5-44f4-96ce-95825d53ff2f",
        "Data": [
            {
                "Time": "2020-09-01T00:00:00+00:00",
                "Value": 101
            },
            {
                "Time": "2020-09-01T00:01:00+00:00",
                "Value": 102
            },
            {
                "Time": "2020-09-01T00:02:00+00:00",
                "Value": 103
            },
            {
                "Time": "2020-09-01T00:03:00+00:00",
                "Value": 104
            },
            {
                "Time": "2020-09-01T00:04:00+00:00",
                "Value": 105
            },
            {
                "Time": "2020-09-01T00:05:00+00:00",
                "Value": 0
            },
            {
                "Time": "2020-09-01T00:06:00+00:00",
                "Value": 0
            },
            {
                "Time": "2020-09-01T00:07:00+00:00",
                "Value": 107
            },
            {
                "Time": "2020-09-01T00:08:00+00:00",
                "Value": 108
            },
            {
                "Time": "2020-09-01T00:09:00+00:00",
                "Value": 109
            }
        ]
    }
}
```

