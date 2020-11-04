**Example 1: 获取角色列表**



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
                "Description": "云审计服务(CA)创建跟踪集功能操作权限含查询和创建对象存储桶(COS)；含查询和创建消息队列CMQ等权限，用以将云审计跟踪日志投递到COS和进行CMQ通知。",
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
                "Description": "蓝鲸自动化运维平台（BlueKing）对您的腾讯云资源进行访问操作，含查询主机信息。",
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

