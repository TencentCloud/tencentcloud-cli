**Example 1: 查询cdb实例cpu使用率**

查询cdb实例cpu使用率

Input: 

```
tccli monitor GetStatisticsBatch --cli-unfold-argument  \
    --Period 5 \
    --MetricName cpu_use_rate \
    --ViewName cdb_detail \
    --Namespace qce/cdb \
    --StartTime 2024-11-26T18:07:32+08:00 \
    --EndTime 2024-11-26T20:10:32+08:00 \
    --Statistics max \
    --Dimensions.0.Dimensions.0.Name instanceid \
    --Dimensions.0.Dimensions.0.Value 0018463a-3bec-11e8-9136-6c0b84be0ace \
    --Dimensions.0.Dimensions.1.Name appid \
    --Dimensions.0.Dimensions.1.Value 0 \
    --Dimensions.0.Dimensions.2.Name insttype \
    --Dimensions.0.Dimensions.2.Value master \
    --Dimensions.0.Dimensions.3.Name projectid \
    --Dimensions.0.Dimensions.3.Value 0
```

Output: 
```
{
    "Response": {
        "StartTime": "2019-03-24T10:50:00+08:00",
        "EndTime": "2019-03-24T20:50:00+08:00",
        "Period": 300,
        "MetricName": "cpu_use_rate",
        "DataPoints": [
            {
                "Dimensions": [
                    {
                        "Name": "instanceid",
                        "Value": "0018463a-3bec-11e8-9136-6c0b84be0ace"
                    },
                    {
                        "Name": "appid",
                        "Value": "0"
                    },
                    {
                        "Name": "insttype",
                        "Value": "master"
                    },
                    {
                        "Name": "projectid",
                        "Value": "0"
                    }
                ],
                "Timestamps": [
                    1535079000,
                    1535079300,
                    1535079600,
                    1535079900,
                    1535080200,
                    1535080500
                ],
                "Values": [
                    2.566,
                    2.283,
                    6.316,
                    2.816,
                    2.7,
                    2.35
                ]
            }
        ],
        "Msg": "",
        "RequestId": "d96ec542-6547-4af2-91ac-fee85c1b8b85"
    }
}
```

