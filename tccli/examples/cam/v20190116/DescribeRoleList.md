**Example 1: Getting the role List**



Input: 

```
tccli cam DescribeRoleList --cli-unfold-argument  \
    --Page 1\
    --Rp 5
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "RoleId": "4611686018427757165",
                "RoleName": "CloudAudit_QCSRole",
                "PolicyDocument": "{\"version\":\"2.0\",\"statement\":[{\"effect\":\"allow\",\"action\":\"name/sts:AssumeRole\",\"principal\":{\"service\":[\"cloudaudit.cloud.tencent.com\"]}}]}",
                “Description”: “CloudAudit (CA)‘s tracking set creation authorization includes permissions to query and create Cloud Object Storage (COS) buckets as well as CMQ message queues. This enables CloudAudit to deliver tracking logs to COS and send CMQ notifications.”,
                "AddTime": "2019-05-17 11:35:02",
                "UpdateTime": "2019-05-17 11:35:02",
                "ConsoleLogin": 0
            },
            {
                "RoleId": "4611686018427733635",
                "RoleName": "testk8u8732u",
                "PolicyDocument": "{\"version\":\"2.0\",\"statement\":[{\"action\":\"name/sts:AssumeRole\",\"effect\":\"allow\",\"principal\":{\"qcs\":\"qcs::cam::uin/909619400:root\"}},{\"action\":\"name/sts:AssumeRole\",\"effect\":\"allow\",\"principal\":{\"qcs\":\"qcs::cam::uin/2385420691:root\"}}]}",
                "Description": "1gfdg4",
                "AddTime": "2019-04-24 16:09:38",
                "UpdateTime": "2019-04-24 16:09:38",
                "ConsoleLogin": 1
            },
            {
                "RoleId": "4611686018427731422",
                "RoleName": "fewfewgcc44",
                "PolicyDocument": "{\"version\":\"2.0\",\"statement\":[{\"action\":\"name/sts:AssumeRole\",\"effect\":\"allow\",\"principal\":{\"qcs\":\"qcs::cam::uin/3374997817:root\"}}]}",
                "Description": "34",
                "AddTime": "2019-04-22 15:25:40",
                "UpdateTime": "2019-04-22 15:25:40",
                "ConsoleLogin": 0
            },
            {
                "RoleId": "4611686018427445962",
                "RoleName": "BK_QcsRole",
                "PolicyDocument": "{\"version\":\"2.0\",\"statement\":[{\"effect\":\"allow\",\"action\":\"name/sts:AssumeRole\",\"principal\":{\"service\":\"blueking.cloud.tencent.com\"}}]}",
                “Description”: “This permission enables BlueKing autonomous OPS platform to access your Tencent Cloud resources and query server information.”,
                "AddTime": "2018-08-24 22:38:39",
                "UpdateTime": "2018-08-24 22:38:39",
                "ConsoleLogin": 0
            },
            {
                "RoleId": "4611686018427424559",
                "RoleName": "testroleName_1263",
                "PolicyDocument": "{\"version\":\"2.0\",\"statement\":[{\"action\":[\"name/sts:AssumeRole\"],\"effect\":\"allow\",\"principal\":{\"qcs\":[\"qcs::cam::uin/2385420691:root\"]}}]}",
                "Description": "testiujjc",
                "AddTime": "2018-08-20 16:30:46",
                "UpdateTime": "2019-04-18 10:37:59",
                "ConsoleLogin": 1
            }
        ],
        "TotalNum": 14,
        "RequestId": "a786b78c-ef8b-4331-b1e5-f287c8b41743"
    }
}
```

