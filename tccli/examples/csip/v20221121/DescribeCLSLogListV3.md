**Example 1: DescribeCLSLogListV3-test1**



Input: 

```
tccli csip DescribeCLSLogListV3 --cli-unfold-argument  \
    --Topics.0.TopicId csip-test-logaccess-251308491-tcss-container_assets \
    --From 1776300037000 \
    --To 1776310037000 \
    --Query * \
    --SyntaxRule 1 \
    --MemberId mem-tencent-testa1b2 \
    --Sort  \
    --Limit 10 \
    --Offset 0 \
    --SamplingRate 1 \
    --HighLight False \
    --UseNewAnalysis False \
    --QueryOptimize 1
```

Output: 
```
{
    "Response": {
        "Analysis": false,
        "AnalysisResults": [],
        "ColNames": [],
        "Context": "Y29udGV4dC1mMzI5ZTc0Ny05NzM1LTRmNDQtYjk4NS1hMDA2NjcwNDMwYWIxNzc2MzEwNjMyMzU2",
        "ListOver": false,
        "Results": [
            {
                "FileName": "",
                "HighLights": [],
                "HostName": "",
                "IndexStatus": "",
                "LogJson": "{\"quuid\":\"95a59821-0b97-4114-a8c6-a42f73ff752e\",\"insert_time\":\"1775739716\",\"host_inner_ip\":\"172.18.10.7\",\"table_id\":\"65490569\",\"table_name\":\"asset_host_info\",\"uuid\":\"95a59821-0b97-4114-a8c6-a42f73ff752e\",\"hostname\":\"QTA_VM\",\"update_time\":\"1776310035\",\"event_type\":\"TCSS_ASSET_HOST\",\"appid\":\"251196288\",\"cls_event_type\":\"asset_host_info\",\"event_mod\":\"MOD\",\"event_time\":\"1776310035\",\"status\":\"ONLINE\"}",
                "PkgId": "",
                "PkgLogId": "",
                "RawLog": "",
                "Source": "21.215.132.152",
                "Time": 1776310036000,
                "TopicId": "89cc4300-c3c5-4011-92c4-6214f59a6169",
                "TopicName": "csip-test-logaccess-251308491-tcss-container_assets"
            }
        ],
        "SamplingRate": 0,
        "Topics": {
            "Errors": [],
            "Infos": [
                {
                    "Context": "Y29udGV4dC1mMzI5ZTc0Ny05NzM1LTRmNDQtYjk4NS1hMDA2NjcwNDMwYWIxNzc2MzEwNjMyMzU2",
                    "Period": 180,
                    "TopicId": "csip-test-logaccess-251308491-tcss-container_assets"
                }
            ]
        },
        "RequestId": "f353404c-3828-442c-9385-5b3373b20c4b"
    }
}
```

**Example 2: DescribeCLSLogListV3-test2**



Input: 

```
tccli csip DescribeCLSLogListV3 --cli-unfold-argument  \
    --From 1776300037000 \
    --To 1776310037000 \
    --Query * \
    --SyntaxRule 1 \
    --Topics.0.TopicId topic-cls-testq \
    --Topics.0.Context context-aa \
    --MemberId mem-tencent-te \
    --Sort desc \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Analysis": false,
        "AnalysisRecords": [
            "{\"level\":\"INFO\",\"count\":1}"
        ],
        "AnalysisResults": [
            {
                "Data": [
                    {
                        "Key": "level",
                        "Value": "INFO"
                    }
                ]
            }
        ],
        "ColNames": [
            "level"
        ],
        "Columns": [
            {
                "Name": "level",
                "Type": "text"
            }
        ],
        "Context": "mock-context",
        "ListOver": true,
        "Results": [
            {
                "FileName": "/var/log/mock.log",
                "HighLights": [
                    {
                        "Key": "msg",
                        "Values": [
                            "mock"
                        ]
                    }
                ],
                "HostName": "mock-host",
                "IndexStatus": "Success",
                "LogJson": "{\"level\":\"INFO\",\"msg\":\"mock log\"}",
                "PkgId": "mock-pkg-id",
                "PkgLogId": "0",
                "RawLog": "mock raw log",
                "Source": "127.0.0.1",
                "Time": 1715692800000,
                "TopicId": "mock-topic-251308491",
                "TopicName": "mock-topic-251308491"
            }
        ],
        "SamplingRate": 1,
        "Topics": {
            "Errors": [
                {
                    "ErrorCodeStr": "MockError",
                    "ErrorMsg": "mock error message",
                    "TopicId": "mock-topic-251308491"
                }
            ],
            "Infos": [
                {
                    "Context": "mock-context",
                    "Period": 7,
                    "TopicId": "mock-topic-251308491"
                }
            ]
        },
        "RequestId": "b7423c66-9780-4a31-9190-f493c64a81b7"
    }
}
```

