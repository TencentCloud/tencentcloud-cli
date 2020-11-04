**Example 1: 查询拨测任务详情示例**



Input: 

```
tccli cat DescribeTaskDetail --cli-unfold-argument  \
    --TaskIds 260229 260230 210837
```

Output: 
```
{
    "Response": {
        "Tasks": [
            {
                "TaskId": 210837,
                "TaskName": "HelpToTestBaidu",
                "CgiUrl": "http://www.baidu.com",
                "CatTypeName": "http",
                "Status": 1,
                "Period": 5,
                "AddTime": "2019-12-11 19:28:58",
                "Type": 2,
                "AlarmStatus": 0,
                "AgentGroupId": 100000003,
                "PolicyGroupId": 0,
                "TopicId": "",
                "Host": "",
                "Port": 0,
                "CheckStr": "",
                "CheckType": 1,
                "UserAgent": "curl",
                "Cookie": "",
                "PostData": "",
                "SslVer": "",
                "IsHeader": 0,
                "DnsSvr": "",
                "DnsCheckIp": "",
                "DnsQueryType": "A",
                "UserName": "",
                "PassWord": "",
                "UseSecConn": 0,
                "NeedAuth": 0,
                "ReqDataType": 0,
                "ReqData": "",
                "RespDataType": 0,
                "RespData": "",
                "RedirectFollowNum": 0
            },
            {
                "TaskId": 260229,
                "TaskName": "SelfTestBaiduModify",
                "CgiUrl": "http://www.baidu.com",
                "CatTypeName": "http",
                "Status": 0,
                "Period": 5,
                "AddTime": "2019-12-12 14:42:00",
                "Type": 0,
                "AlarmStatus": 0,
                "AgentGroupId": 100004185,
                "PolicyGroupId": 3231435,
                "TopicId": "",
                "Host": "",
                "Port": 0,
                "CheckStr": "",
                "CheckType": 1,
                "UserAgent": "curl",
                "Cookie": "",
                "PostData": "",
                "SslVer": "",
                "IsHeader": 0,
                "DnsSvr": "",
                "DnsCheckIp": "",
                "DnsQueryType": "A",
                "UserName": "",
                "PassWord": "",
                "UseSecConn": 0,
                "NeedAuth": 0,
                "ReqDataType": 0,
                "ReqData": "",
                "RespDataType": 0,
                "RespData": "",
                "RedirectFollowNum": 2
            },
            {
                "TaskId": 260230,
                "TaskName": "SelfTestBaiduModifyEx",
                "CgiUrl": "http://www.baidu.com",
                "CatTypeName": "http",
                "Status": 0,
                "Period": 5,
                "AddTime": "2019-12-12 14:42:24",
                "Type": 2,
                "AlarmStatus": 0,
                "AgentGroupId": 100000003,
                "PolicyGroupId": 0,
                "TopicId": "",
                "Host": "",
                "Port": 0,
                "CheckStr": "",
                "CheckType": 1,
                "UserAgent": "curl",
                "Cookie": "",
                "PostData": "",
                "SslVer": "",
                "IsHeader": 0,
                "DnsSvr": "",
                "DnsCheckIp": "",
                "DnsQueryType": "A",
                "UserName": "",
                "PassWord": "",
                "UseSecConn": 0,
                "NeedAuth": 0,
                "ReqDataType": 0,
                "ReqData": "",
                "RespDataType": 0,
                "RespData": "",
                "RedirectFollowNum": 2
            }
        ],
        "RequestId": "0233fd07-5052-4f3b-af88-b5d26cca8868"
    }
}
```

