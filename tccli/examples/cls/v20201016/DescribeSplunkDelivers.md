**Example 1: 查询Splunk投递任务**



Input: 

```
tccli cls DescribeSplunkDelivers --cli-unfold-argument  \
    --TopicId d1d7d473-827e-4dad-9a42-f0287ad43125 \
    --Filters.0.Key taskId \
    --Filters.0.Values 46bb8292-1974-4663-8ce5-498256a42431
```

Output: 
```
{
    "Response": {
        "Infos": [
            {
                "CreateTime": 1757657329,
                "Enable": 1,
                "HasServiceLog": 2,
                "Index": "",
                "IndexAck": 1,
                "Metadata": {
                    "Format": "json"
                },
                "Name": "name-test14",
                "NetInfo": {
                    "Host": "10.0.0.112",
                    "IsSSL": true,
                    "NetType": 1,
                    "Port": 8088,
                    "Token": "59f9b80c-ae2f-43c1-8c93-436094343125",
                    "VirtualGatewayType": 0,
                    "VpcId": "vpc-k1bdf0es"
                },
                "Source": "",
                "SourceType": "",
                "Status": 1,
                "TaskId": "46bb8292-1974-4663-8ce5-498256a42431",
                "TopicId": "d1d7d473-827e-4dad-9a42-f0287ad43125",
                "Uin": 100001127589,
                "UpdateTime": 1757657329,
                "DSLFilter": "log_keep(op_str_eq(v(\"type\"), \"kibana_stats\"))"
            }
        ],
        "RequestId": "964ff3ff-ec82-40d2-90ab-bb9b8bc43125",
        "Total": 1
    }
}
```

**Example 2: 查询Splunk投递任务-包含ExternalRole信息**



Input: 

```
tccli cls DescribeSplunkDelivers --cli-unfold-argument  \
    --TopicId 6b81282d-f355-404f-ae1f-6e00b27dfc70
```

Output: 
```
{
    "Response": {
        "Infos": [
            {
                "Channel": "",
                "CreateTime": 1772715227,
                "Enable": 1,
                "ExternalRole": {
                    "ExternalId": "testsplunk",
                    "RoleArn": "qcs::cam::uin/1000011275:roleName/splunk"
                },
                "HasServiceLog": 2,
                "Index": "",
                "IndexAck": 1,
                "Metadata": {
                    "EnableTag": true,
                    "Format": "json",
                    "TagJsonTiled": true
                },
                "Name": "SplunkTask",
                "NetInfo": {
                    "Host": "10.0.0.113",
                    "IsSSL": true,
                    "NetType": 1,
                    "Port": 8088,
                    "Token": "59f9b80c-ae2f-43c1-8c93-436094323e",
                    "VirtualGatewayType": 0,
                    "VpcId": "vpc-k1bdf0"
                },
                "Source": "",
                "SourceType": "",
                "Status": 1,
                "TaskId": "565a2f82-22d3-4f2e-b417-0e251805c6",
                "TopicId": "6b81282d-f355-404f-ae1f-6e00b27dfc",
                "Uin": 1000010010,
                "UpdateTime": 1772715227
            }
        ],
        "Total": 1,
        "RequestId": "7b8bee46-7f7f-4551-9e2c-2e5766e8bb2a"
    }
}
```

